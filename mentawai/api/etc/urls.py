from django.conf.urls import patterns, url

from .views import GetHomeData


urlpatterns = patterns('',
    url(r'^get-home-data$', GetHomeData.as_view(), name='get_home_data'),
)
