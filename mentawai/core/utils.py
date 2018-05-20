import hashlib
import json
import os
import requests

from django.conf import settings
from django.contrib.auth import login
from django.template.defaultfilters import slugify
from django.utils import timezone

from requests.exceptions import ConnectionError, Timeout

import phonenumbers

from mentawai.core.exceptions import DokuPaymentError


class FilenameGenerator(object):
    """
    Utility class to handle generation of file upload path
    """
    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, instance, filename):
        today = timezone.localtime(timezone.now()).date()

        filepath = os.path.basename(filename)
        filename, extension = os.path.splitext(filepath)
        filename = slugify(filename)

        path = "/".join([
            self.prefix,
            str(today.year),
            str(today.month),
            str(today.day),
            filename + extension
        ])
        return path


try:
    from django.utils.deconstruct import deconstructible
    FilenameGenerator = deconstructible(FilenameGenerator)
except ImportError:
    pass


def normalize_phone(number):
    number = number[1:] if number[:1] == '0' else number
    parse_phone_number = phonenumbers.parse(number, 'ID')
    phone_number = phonenumbers.format_number(
        parse_phone_number, phonenumbers.PhoneNumberFormat.E164)
    return phone_number


def force_login(request, user):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)


def create_word(amount, invoice, token, pairing_code, device_id):
    return hashlib.sha1('%s%s%s%s%s%s%s%s' % (
        amount, settings.DOKU_MERCHANT_ID, settings.DOKU_SHARED_KEY,
        invoice, '360', token, pairing_code, device_id)).hexdigest()


def charge_doku(data, user):
    words = create_word(
        data['res_amount'], data['res_transaction_id'], data['res_token_id'],
        data['res_pairing_code'], data['res_device_id']
    )

    current_time = timezone.localtime(timezone.now())

    params = {
        'req_mall_id': settings.DOKU_MERCHANT_ID,
        'req_chain_merchant': 'NA',
        'req_amount': data['res_amount'],
        'req_words': words,
        'req_purchase_amount': data['res_amount'],
        'req_trans_id_merchant': data['res_transaction_id'],
        'req_request_date_time': current_time.strftime('%Y%m%d%H%I%S'),
        'req_currency': '360',
        'req_purchase_currency': '360',
        'req_session_id': hashlib.sha1(current_time.strftime('%Y%m%d%H%I%S')).hexdigest(),
        'req_name': data['res_name'],
        'req_payment_channel': data['res_payment_channel'],
        'req_basket': '%s,%s,%s,%s' % ('retribusi', data['res_amount'], '1', data['res_amount']),
        'req_address': user.nationaly,
        'req_email': data['res_data_email'],
        'req_token_id': data['res_token_id'],
        'req_mobile_phone': user.mobile_number,
    }

    params = json.dumps(params).strip(' ')

    try:
        response = requests.post(url=settings.DOKU_PAYMENT_URL,
                                 data={'data': params})
        response_json = response.json()
    except (ConnectionError, Timeout):
        raise DokuPaymentError("Connection Timeout, can't connect to DOKU")

    if response.status_code != 200:
        raise DokuPaymentError('Invalid Data')

    if response_json['res_response_msg'] != 'SUCCESS':
        raise DokuPaymentError("Error from DOKU, unable to charge")

    return response
