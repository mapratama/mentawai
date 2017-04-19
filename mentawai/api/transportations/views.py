from mentawai.api.response import ErrorResponse
from mentawai.api.views import SessionAPIView
from mentawai.apps.transportations.models import Transportation
from mentawai.core.serializers import serialize_transportation

from rest_framework import status
from rest_framework.response import Response


class Details(SessionAPIView):
    def get(self, request, id):
        try:
            transportation = Transportation.objects.get(id=id)
        except:
            return ErrorResponse(error_description='Transportation Not Found')

        return Response({'transportations': serialize_transportation(transportation)},
                        status=status.HTTP_200_OK)
