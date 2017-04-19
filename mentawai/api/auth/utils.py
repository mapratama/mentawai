from mentawai.apps.banners.models import Banner
from mentawai.apps.partners.models import Partner
from mentawai.apps.newses.models import News
from mentawai.apps.tours.models import Tour
from mentawai.apps.transportations.models import Transportation
from mentawai.apps.resorts.models import Resort
from mentawai.apps.waves.models import Wave
from mentawai.apps.weathers.models import Weather

from mentawai.core.serializers import (serialize_user, serialize_weather,
                                       serialize_wave, serialize_news,
                                       serialize_resort, serialize_transportation,
                                       serialize_tour, serialize_partner,
                                       serialize_banner)


def success_response(user, session_key):
    banners = [serialize_banner(banner) for banner in Banner.objects.is_active()]
    partners = [serialize_partner(partner) for partner in Partner.objects.is_active()]
    newses = [serialize_news(news) for news in News.objects.is_active()]
    resorts = [serialize_resort(resort) for resort in Resort.objects.is_active()]
    tours = [serialize_tour(tour) for tour in Tour.objects.is_active()]
    waves = [serialize_wave(wave) for wave in Wave.objects.is_active()]
    weathers = [serialize_weather(weather) for weather in Weather.objects.is_future()]
    transportations = [serialize_transportation(transportation)
                       for transportation in Transportation.objects.is_active()]

    response = {
        'session_key': session_key,
        'user': serialize_user(user),
        'banners': banners,
        'partners': partners,
        'newses': newses,
        'resorts': resorts,
        'tours': tours,
        'transportations': transportations,
        'waves': waves,
        'weathers': weathers
    }

    return response
