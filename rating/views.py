from django.shortcuts import render

from .models import *
from .forms import RatingForm


def index(request):
    location_list = Location.objects.all()
    return render(request, 'rating/index.html', {'location_list': location_list, })


def city(request, location_id):
    cinema_list = Cinema.objects.filter(parent_id=location_id)
    data = {
        'cinema_list': cinema_list,
        'city': Location.objects.get(id=location_id).city}
    return render(request, 'rating/city.html', data)


def cinema(request, location_id, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    hall_list = Hall.objects.filter(parent=cinema)

    data = {
        'hall_list': hall_list,
        'city': Location.objects.get(id=location_id).city,
        'cinema': Cinema.objects.get(id=cinema_id).name
    }
    return render(request, 'rating/cinema.html', data)


def hall(request, location_id, cinema_id, hall_id):
    row_list = Row.objects.filter(parent_id=hall_id)

    data = {
        'row_list': row_list,
        'hall': Hall.objects.get(id=hall_id).name
    }

    return render(request, 'rating/hall.html', data)


def seat(request, location_id, cinema_id, hall_id, seat_id):
    seat_details = Seat.objects.get(id=seat_id)

    return render(request, 'rating/seat.html', {'seat': seat_details})


def rating(request):
    return render(request, 'index')


def rate(request, location_id, cinema_id, hall_id, seat_id):
    seat_details = Seat.objects.get(id=seat_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.seat = seat_details
            rating.save()
        return render(request, 'rating/seat.html', {'seat': seat_details})

    form = RatingForm()

    data = {
        'seat': seat_details,
        'form': form,
    }

    return render(request, 'rating/rate.html', data)
