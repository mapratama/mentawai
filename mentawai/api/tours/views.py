from mentawai.api.response import ErrorResponse
from mentawai.api.views import SessionAPIView
from mentawai.apps.tours.models import Tour
from mentawai.core.serializers import serialize_tour

from rest_framework import status
from rest_framework.response import Response


class TourList(SessionAPIView):

    def get(self, request):
        tours = [serialize_tour(tour) for tour in Tour.objects.is_active()]
        return Response({'tours': tours}, status=status.HTTP_200_OK)


class Details(SessionAPIView):
    def get(self, request, id):
        try:
            tour = Tour.objects.get(id=id)
        except:
            return ErrorResponse(error_description='Tour Not Found')

        return Response({'tour': serialize_tour(tour)}, status=status.HTTP_200_OK)
