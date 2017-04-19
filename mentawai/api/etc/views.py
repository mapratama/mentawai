from mentawai.apps.banners.models import Banner
from mentawai.apps.newses.models import News
from mentawai.apps.weathers.models import Weather
from mentawai.api.views import SessionAPIView
from mentawai.core.serializers import (serialize_weather, serialize_news,
                                       serialize_banner)

from rest_framework import status
from rest_framework.response import Response


class GetHomeData(SessionAPIView):

    def get(self, request):
        banners = [serialize_banner(banner) for banner in Banner.objects.is_active()]
        newses = [serialize_news(news) for news in News.objects.is_active()]
        weathers = [serialize_weather(weather) for weather in Weather.objects.is_future()]

        response = {
            'banners': banners,
            'newses': newses,
            'weathers': weathers,
        }

        return Response(response, status=status.HTTP_200_OK)
