from django.conf.urls import include, patterns, url


urlpatterns = patterns('mentawai.api.views',
    url(r'^auth/', include('mentawai.api.auth.urls', namespace='auth')),
    url(r'^contents/', include('mentawai.api.contents.urls', namespace='contents')),
    url(r'^payments/', include('mentawai.api.payments.urls', namespace='payments')),
)
