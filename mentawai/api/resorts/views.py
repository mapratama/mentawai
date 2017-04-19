from mentawai.api.response import ErrorResponse
from mentawai.api.views import SessionAPIView
from mentawai.apps.resorts.models import Resort
from mentawai.core.serializers import serialize_resort

from rest_framework import status
from rest_framework.response import Response


class Details(SessionAPIView):
    def get(self, request, id):
        try:
            resort = Resort.objects.get(id=id)
        except:
            return ErrorResponse(error_description='Resort Not Found')

        return Response({'resort': serialize_resort(resort)}, status=status.HTTP_200_OK)
