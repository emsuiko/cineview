from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^location/(?P<location_id>[0-9]+)/$', views.city, name='city'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/$', views.cinema, name='cinema'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/view/(?P<view>[2|3]?)/$', views.hall, name='hall'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/rows/view/(?P<view>[2|3]?)/$', views.rows, name='row'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/view/(?P<view>[2|3]?)/seat/(?P<seat_id>[0-9]+)/$', views.seat, name='seat'),
    url(r'^location/(?P<location_id>[0-9]+)/cinema/(?P<cinema_id>[0-9]+)/hall/(?P<hall_id>[0-9]+)/view/(?P<view>[2|3]?)/seat/(?P<seat_id>[0-9]+)/rate$', views.rate, name='rate'),
    url(r'^nested_admin/', include('nested_admin.urls')),
]