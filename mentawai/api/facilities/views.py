from mentawai.apps.resorts.models import Resort
from mentawai.apps.transportations.models import Transportation
from mentawai.api.views import SessionAPIView
from mentawai.core.serializers import serialize_resort, serialize_transportation

from rest_framework import status
from rest_framework.response import Response


class FacilityList(SessionAPIView):

    def get(self, request):
        resorts = [serialize_resort(resort) for resort in Resort.objects.is_active()]
        transportations = [serialize_transportation(transportation)
                           for transportation in Transportation.objects.is_active()]

        response = {
            'resorts': resorts,
            'transportations': transportations
        }

        return Response(response, status=status.HTTP_200_OK)
