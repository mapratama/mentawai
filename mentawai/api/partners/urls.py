from django.conf.urls import patterns, url

from .views import PartnerList


urlpatterns = patterns('',
    url(r'^$', PartnerList.as_view(), name='index'),
)
