from mentawai.apps.partners.models import Partner
from mentawai.api.views import SessionAPIView
from mentawai.core.serializers import serialize_partner

from rest_framework import status
from rest_framework.response import Response


class PartnerList(SessionAPIView):

    def get(self, request):
        partners = [serialize_partner(partner) for partner in Partner.objects.is_active()]
        return Response({'partners': partners}, status=status.HTTP_200_OK)
