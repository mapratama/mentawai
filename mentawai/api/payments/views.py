import json
import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.shortcuts import get_object_or_404

from mentawai.api.views import MidtransAPIView
from mentawai.apps.payment_histories.models import PaymentHistory


class Notification(APIView):

    def post(self, request):
        """ View to handle notification webhook from Midtrans
            https://api-docs.midtrans.com/#best-practice-to-handle-notification
            1. Validate signature
            2. IDEMPOTENT - Multiple notification can be sent
        """

        '''
        # Validate request's signature
        signature_key = "{}{}{}{}".format(
            request.data.get('order_id'), request.data.get('status_code'),
            request.data.get('gross_amount'), settings.VERITRANS_SERVER_KEY
        )
        expected_signature = sha512(signature_key).hexdigest()
        if expected_signature != request.data.get('signature_key'):
            return ErrorResponse()
        '''

        payment_history = get_object_or_404(
            PaymentHistory,
            veritrans_transaction_id=request.data.get('order_id', None)
        )

        # Notify anomali admin for manual accept / deny
        if request.data["fraud_status"] == "challenge":
            # TODO: notification method
            return Response({}, status=status.HTTP_200_OK)

        # Canceled / denied
        if request.data["transaction_status"] in ["cancel", "deny"]:
            payment_history.status = PaymentHistory.STATUS.failed
            payment_history.error_log = json.dumps(request.data)
            payment_history.save(update_fields=['status', 'error_log'])
            return Response({}, status=status.HTTP_200_OK)

        # Accepted, also make sure we do not process this balance_update twice
        if (request.data["transaction_status"] in ["capture", "settlement"] and
            request.data["fraud_status"] == "accept"):  # noqa
            payment_history.status = PaymentHistory.STATUS.completed
            payment_history.save(update_fields=['status'])
            return Response({}, status=status.HTTP_200_OK)

        return Response({}, status=status.HTTP_200_OK)


class Charge(MidtransAPIView):

    def post(self, request):
        data = request.data
        transaction_details = data['transaction_details']
        request.user.payment_histories.create(value=transaction_details['gross_amount'],
                                              payment_id=transaction_details['order_id'])

        if settings.TEST:
            return Response({"token": "12345abcdef"}, status=status.HTTP_200_OK)

        response = requests.post(settings.MIDTRANS_BASE_URL, headers=settings.MIDTRANS_HEADERS,
                                 data=json.dumps(data))

        return Response(json.loads(response.content), status=status.HTTP_200_OK)
