from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^smsweather/', include('smsweather.urls')),
)
