from mentawai.api.response import ErrorResponse
from mentawai.api.views import MentawaiAPIView, SessionAPIView
from mentawai.core.utils import force_login

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from rest_framework import status
from rest_framework.response import Response

from .forms import APIRegistrationForm
from .utils import success_response


class Login(MentawaiAPIView):

    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            login(request, form.get_user())
            user = request.user

            push_notification_key = request.data.get('push_notification_key')
            if push_notification_key:
                user.push_notification_key = push_notification_key
                user.save(update_fields=['push_notification_key'])

            return Response(success_response(user, request.session.session_key),
                            status=status.HTTP_200_OK)
        return ErrorResponse(form=form)


class Register(MentawaiAPIView):

    def post(self, request):
        form = APIRegistrationForm(data=request.data)
        if form.is_valid():
            user = form.save()
            force_login(request, user)
            request.session.create()
            return Response(success_response(user, request.session.session_key),
                            status=status.HTTP_200_OK)
        return ErrorResponse(form=form)


class Logout(SessionAPIView):

    def post(self, request):
        logout(request)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)


class NotificationUpdate(SessionAPIView):

    def post(self, request):
        user = request.user
        user.gcm_key = request.data['gcm_key']
        user.save()

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
