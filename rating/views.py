from django.shortcuts import render

from .models import *


def index(request):
    location_list = Location.objects.all()
    return render(request, 'rating/index.html', {'location_list': location_list, })


def city(request, location_id):
    cinema_list = Cinema.objects.filter(location_id=location_id)
    data = {
        'cinema_list': cinema_list,
        'city': Location.objects.get(id=location_id).city}
    return render(request, 'rating/city.html', data)


def cinema(request, location_id, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    hall_list = Hall.objects.filter(cinema=cinema)

    data = {
        'hall_list': hall_list,
        'cinema': Cinema.objects.get(id=cinema_id).name
    }
    return render(request, 'rating/cinema.html', data)


def hall(request, location_id, cinema_id, hall_id):
    row_list = Row.objects.filter(hall__id=hall_id)

    data = {
        'row_list': row_list,
        'hall': Hall.objects.get(id=hall_id).name
    }

    return render(request, 'rating/hall.html', data)


def seat(request, location_id, cinema_id, hall_id, seat_id):
    seat_details = Seat.objects.get(id=seat_id)

    data = {
        'seat': seat_details,
    }

    return render(request, 'rating/seat.html', data)

