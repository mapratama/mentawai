from django.conf.urls import patterns, url

from .views import TourList, Details


urlpatterns = patterns('',
    url(r'^$', TourList.as_view(), name='index'),
    url(r'^(?P<id>\d+)$', Details.as_view(), name='details'),
)
