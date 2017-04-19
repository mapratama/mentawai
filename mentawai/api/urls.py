from django.conf.urls import include, patterns, url


urlpatterns = patterns('mentawai.api.views',
    url(r'^auth/', include('mentawai.api.auth.urls', namespace='auth')),
)
