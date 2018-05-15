from rest_framework import status
from rest_framework.response import Response

from mentawai.api.views import SessionAPIView
from mentawai.core.serializers import serialize_user, serialize_payment


class Details(SessionAPIView):

    def get(self, request):
        response = serialize_user(request.user)

        payment = request.user.get_payment_active()
        if payment:
            response['payment'] = serialize_payment(payment)

        return Response(response, status=status.HTTP_200_OK)
