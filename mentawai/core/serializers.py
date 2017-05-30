from django.conf import settings


def serialize_user(user):
    return {
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'mobile_number': user.mobile_number,
        'gender': user.gender,
        'birthday': user.birthday.isoformat() if user.birthday else None,
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
