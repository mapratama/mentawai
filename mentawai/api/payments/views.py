from mentawai.api.views import SessionAPIView
from mentawai.api.response import ErrorResponse
from mentawai.core.serializers import serialize_payment
from mentawai.core.utils import charge_doku

from rest_framework import status
from rest_framework.response import Response

from .forms import PaymentForm


class Pay(SessionAPIView):

    def post(self, request):
        form = PaymentForm(data=request.data)
        if form.is_valid():
            payment = form.save(request.user)
            charge_doku(request.data, payment)
            return Response(serialize_payment(payment), status=status.HTTP_200_OK)
        return ErrorResponse(form=form)
