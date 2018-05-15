from django.conf.urls import patterns, url

from .views import Details

urlpatterns = patterns('',
    url(r'^$', Details.as_view(), name='details')
)
