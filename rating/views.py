from django.shortcuts import render

from .models import *
from .forms import RatingForm


def index(request):
    location_list = Location.objects.all()
    return render(request, 'rating/index.html', {'location_list': location_list, })


def city(request, location_id):
    cinema_list = Cinema.objects.filter(parent_id=location_id)

    location = Location.objects.get(id=location_id)

    data = {
        'cinema_list': cinema_list,
        'city': location.city,
        'breadcrumbs': location.breadcrumbs()
    }
    return render(request, 'rating/city.html', data)


def cinema(request, location_id, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    hall_list = Hall.objects.filter(parent=cinema)

    data = {
        'hall_list': hall_list,
        'city': Location.objects.get(id=location_id).city,
        'cinema': Cinema.objects.get(id=cinema_id).name,
        'breadcrumbs': cinema.breadcrumbs()
    }
    return render(request, 'rating/cinema.html', data)


def hall(request, location_id, cinema_id, hall_id, view):
    row_list = Row.objects.filter(parent_id=hall_id).order_by('number')

    hall = Hall.objects.get(id=hall_id)

    data = {
        'row_list': row_list,
        'hall': hall,
        'view': view,
        'breadcrumbs': hall.breadcrumbs()
    }

    return render(request, 'rating/hall.html', data)


def rows(request, location_id, cinema_id, hall_id, view):
    row_list = Row.objects.filter(parent_id=hall_id).order_by('number')

    hall = Hall.objects.get(id=hall_id)

    data = {
        'row_list': row_list,
        'hall': hall,
        'view': view,
        'breadcrumbs': hall.breadcrumbs()
    }

    return render(request, 'rating/rows.html', data)


def seat(request, location_id, cinema_id, hall_id, view, seat_id):
    seat_details = Seat.objects.get(id=seat_id)

    ratings_2d, ratings_3d = [], []
    for i in range(1, 5):
        single_rating = {
            'title': i,
            'total': seat_details.ratings_2d_detail(i),
            'comments': seat_details.rating_2d_comments(i),
        }
        ratings_2d.append(single_rating)

        single_rating2 = {
            'title': i,
            'total': seat_details.ratings_3d_detail(i),
            'comments': seat_details.rating_3d_comments(i),
        }
        ratings_3d.append(single_rating2)

    data = {
        'seat': seat_details,
        'breadcrumbs': seat_details.breadcrumbs(),
        'ratings_2d': ratings_2d,
        'ratings_3d': ratings_3d
    }

    print(data)

    return render(request, 'rating/seat.html', data)


def rating(request):
    return render(request, 'index')


def rate(request, location_id, cinema_id, hall_id, view, seat_id):
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
        'breadcrumbs': seat_details.breadcrumbs()
    }

    return render(request, 'rating/rate.html', data)
