from mentawai.api.views import SessionAPIView
from mentawai.api.response import ErrorResponse
from mentawai.core.serializers import serialize_payment
from mentawai.core.utils import charge_doku

from rest_framework import status
from rest_framework.response import Response

from mentawai.core.exceptions import DokuPaymentError

from .forms import PaymentForm


class Pay(SessionAPIView):

    def post(self, request):
        form = PaymentForm(data=request.data)
        if form.is_valid():
            payment = form.save(request.user)

            try:
                charge_doku(request.data, payment)
            except DokuPaymentError as error:
                return ErrorResponse(error_description=error)

            return Response(serialize_payment(payment), status=status.HTTP_200_OK)
        return ErrorResponse(form=form)
