import calendar

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


def serialize_weather(weather):
    return {
        'id': weather.id,
        'date': calendar.timegm(weather.date.utctimetuple()),
        'description': weather.description,
        'temperature': weather.temperature,
        'humidity': weather.humidity,
        'wind_velocity': weather.wind_velocity,
        'wind_direction': weather.wind_direction,
    }


def serialize_location(location):
    return {
        'id': location.id,
        'name': location.name,
    }


def serialize_banner(banner):
    photo_url = settings.HOST + banner.photo.thumbnails.get('size_600x300').url \
        if banner.photo else None

    return {
        'id': banner.id,
        'photo_url': photo_url,
        'is_active': banner.is_active,
    }


def serialize_partner(partner):
    photo_url = settings.HOST + partner.photo.thumbnails.get('size_600x300').url \
        if partner.photo else None

    return {
        'id': partner.id,
        'name': partner.name,
        'decription': partner.decription if partner.description else None,
        'website': partner.website if partner.website else None,
        'photo_url': photo_url,
        'is_active': partner.is_active,
    }


def serialize_wave(wave):
    photo_url = settings.HOST + wave.photo.thumbnails.get('size_600x300').url \
        if wave.photo else None

    return {
        'id': wave.id,
        'name': wave.name,
        'type': wave.type,
        'lat': wave.lat,
        'long': wave.long,
        'address': wave.address if wave.address else None,
        'photo_url': photo_url,
        'location': serialize_location(wave.location),
        'is_active': wave.is_active,
    }


def serialize_news(news):
    photo_url = settings.HOST + news.photo.thumbnails.get('size_600x300').url \
        if news.photo else None

    return {
        'id': news.id,
        'title': news.title,
        'content': news.content if news.content else None,
        'photo_url': photo_url,
        'is_active': news.is_active,
    }


def serialize_tour(tour):
    photo_url = settings.HOST + tour.photo.thumbnails.get('size_600x300').url \
        if tour.photo else None

    return {
        'id': tour.id,
        'name': tour.name,
        'type': tour.type,
        'location': serialize_location(tour.location),
        'description': tour.description if tour.description else None,
        'address': tour.address if tour.address else None,
        'lat': tour.lat if tour.lat else None,
        'long': tour.long if tour.long else None,
        'photo_url': photo_url,
        'is_active': tour.is_active,
    }


def serialize_resort(resort):
    photo_url = settings.HOST + resort.photo.thumbnails.get('size_600x300').url \
        if resort.photo else None

    return {
        'id': resort.id,
        'name': resort.name,
        'location': serialize_location(resort.location),
        'address': resort.address if resort.address else None,
        'website': resort.website if resort.website else None,
        'phone': resort.phone if resort.phone else None,
        'lat': resort.lat if resort.lat else None,
        'long': resort.long if resort.long else None,
        'photo_url': photo_url,
        'is_active': resort.is_active,
    }


def serialize_transportation(transportation):
    photo_url = settings.HOST + transportation.photo.thumbnails.get('size_600x300').url \
        if transportation.photo else None

    return {
        'id': transportation.id,
        'name': transportation.name,
        'type': transportation.type,
        'day': transportation.day,
        'departure_time': str(transportation.departure_time) if transportation.departure_time else None,
        'arrived_time': str(transportation.arrived_time) if transportation.arrived_time else None,
        'pickup_location': transportation.pickup_location,
        'destination': transportation.destination,
        'photo_url': photo_url,
        'is_active': transportation.is_active,
    }
