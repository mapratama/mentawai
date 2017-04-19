from django.conf.urls import patterns, url

from .views import FacilityList


urlpatterns = patterns('',
    url(r'^$', FacilityList.as_view(), name='index'),
)
