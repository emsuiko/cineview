from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/(?P<location_id>[0-9]+)/$', views.city, name='city'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/$', views.cinema, name='cinema'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/$', views.hall, name='hall'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/seat/(?P<seat_id>[0-9]+)/$', views.seat, name='seat'),
]