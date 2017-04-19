from mentawai.apps.waves.models import Wave
from mentawai.api.views import SessionAPIView
from mentawai.core.serializers import serialize_wave

from rest_framework import status
from rest_framework.response import Response


class WaveList(SessionAPIView):

    def get(self, request):
        waves = [serialize_wave(wave) for wave in Wave.objects.is_active()]
        return Response({'waves': waves}, status=status.HTTP_200_OK)
