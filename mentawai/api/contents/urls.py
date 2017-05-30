from django.conf.urls import patterns, url

from .views import Sync

urlpatterns = patterns('',
    url(r'^$', Sync.as_view(), name='sync')
)
