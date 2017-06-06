import calendar

from django.conf import settings


def serialize_user(user):
    return {
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'mobile_number': user.mobile_number,
        'gender': user.gender,
        'nationaly': user.nationaly,
        'pasport_number': user.pasport_number,
    }


def serialize_payment(payment):
    return {
        'id': payment.id,
        'status': payment.status,
        'number_of_visits': payment.number_of_visits,
        'value': payment.value,
        'payment_id': payment.payment_id,
        'created': calendar.timegm(payment.created.utctimetuple()),
    }


def serialize_content(content):
    return {
        'id': content.id,
        'name': content.name,
        'key': content.key,
        'description': content.description,
        'photos': [serialize_photo(photo) for photo in content.photos.all()]
    }


def serialize_photo(photo):
    photo_url = settings.HOST + photo.photo.thumbnails.get('size_500x350').url \
        if photo.photo else None

    return {
        'id': photo.id,
        'photo_url': photo_url,
        'name': photo.name,
    }
