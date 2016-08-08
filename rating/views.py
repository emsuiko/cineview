from django.shortcuts import render

from .models import *


def index(request):
    cinema_list = Cinema.objects.all()
    return render(request, 'rating/index.html', {'cinema_list': cinema_list, })


def cinema(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    hall_list = Hall.objects.filter(cinema=cinema)

    return render(request, 'rating/cinema.html', {'hall_list': hall_list, })


def hall(request, cinema_id, hall_id):
    row_list = Row.objects.filter(hall__id=hall_id)
    return render(request, 'rating/hall.html', {'row_list': row_list, })


def seat(request, cinema_id, hall_id, seat_id):
    seat_details = Seat.objects.get(id=seat_id)
    return render(request, 'rating/seat.html', {'seat': seat_details, })

