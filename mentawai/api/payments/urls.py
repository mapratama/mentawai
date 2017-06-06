from django.conf.urls import patterns, url

from .views import Pay

urlpatterns = patterns('',
    url(r'^pay$', Pay.as_view(), name='pay'),
)
