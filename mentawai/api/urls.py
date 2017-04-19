from django.conf.urls import include, patterns, url


urlpatterns = patterns('mentawai.api.views',
    url(r'^auth/', include('mentawai.api.auth.urls', namespace='auth')),
    url(r'^etc/', include('mentawai.api.etc.urls', namespace='etc')),
    url(r'^facilities/', include('mentawai.api.facilities.urls', namespace='facilities')),
    url(r'^partners/', include('mentawai.api.partners.urls', namespace='partners')),
    url(r'^newses/', include('mentawai.api.newses.urls', namespace='newses')),
    url(r'^resorts/', include('mentawai.api.resorts.urls', namespace='resorts')),
    url(r'^tours/', include('mentawai.api.tours.urls', namespace='tours')),
    url(r'^transportations/', include('mentawai.api.transportations.urls', namespace='transportations')),
    url(r'^waves/', include('mentawai.api.waves.urls', namespace='waves')),
)
