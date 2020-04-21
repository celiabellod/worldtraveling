
from django.urls import path, include, re_path
from store import views
from django.conf.urls import url

urlpatterns = [
    url(r'^travel/(?P<pk>\d+)$', views.Detail.as_view(), name='detail'),
    url(r'^contact/(?P<travel_id>\d+)?', views.contact, name='contact'),
    url(r'^booking/(?P<travel_id>\d+)$', views.booking, name='booking'),

]
