from django.conf.urls import patterns, url

from smsweather import views

urlpatterns = patterns('',
    # ex : /smsweather/
    url(r'^$', views.index, name='index'),
    url(r'^twilio/$', views.postweather, name='postweather'),
    # ex : /smsweather/Madison
    url(r'^(?P<location>\w+)/$', views.getweather, name='getweather'),    
)