from mentawai.api.response import ErrorResponse
from mentawai.api.views import SessionAPIView
from mentawai.apps.newses.models import News
from mentawai.core.serializers import serialize_news

from rest_framework import status
from rest_framework.response import Response


class Details(SessionAPIView):
    def get(self, request, id):
        try:
            news = News.objects.get(id=id)
        except:
            return ErrorResponse(error_description='News Not Found')

        return Response({'news': serialize_news(news)}, status=status.HTTP_200_OK)
