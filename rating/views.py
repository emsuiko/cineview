from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    cinema_list = Cinema.objects.all()
    template = loader.get_template('rating/index.html')
    context = {
        'cinema_list': cinema_list,
    }
    return HttpResponse(template.render(context, request))


def cinema(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    hall_list = Hall.objects.filter(cinema=cinema)

    template = loader.get_template('rating/cinema.html')
    context = {
        'hall_list': hall_list,
    }
    return HttpResponse(template.render(context, request))


def hall(request, cinema_id, hall_id):
    row_list = Row.objects.filter(hall__id=hall_id)

    template = loader.get_template('rating/hall.html')
    context = {
        'row_list': row_list,
    }
    return HttpResponse(template.render(context, request))


def seat(request, cinema_id, hall_id, seat_id):
    seat = Seat.objects.get(id=seat_id)

    template = loader.get_template('rating/seat.html')
    context = {
        'seat': seat,
    }
    return HttpResponse(template.render(context, request))

