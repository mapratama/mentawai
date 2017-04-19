from django.conf.urls import patterns, url

from .views import WaveList


urlpatterns = patterns('',
    url(r'^$', WaveList.as_view(), name='index'),
)
