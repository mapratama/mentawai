from django.conf.urls import patterns, url

from .views import Charge, Notification

urlpatterns = patterns('',
    url(r'^charge$', Charge.as_view(), name='charge'),
    url(r'^midtrans-notification$', Notification.as_view(), name='notification'),
)
