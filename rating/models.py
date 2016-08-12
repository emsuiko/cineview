from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.city


class Cinema(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.name


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.name


class Row(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

    def __str__(self):
        return "%s" % self.number


class Seat(models.Model):
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

    def calculated_2d_rating(self):
        values = self.rating_set.values_list('view_2d', flat=True)
        if len(values) == 0:
            return None
        else:
            return sum(values) / len(values)

    def calculated_3d_rating(self):
        values = self.rating_set.values_list('view_3d', flat=True)
        if len(values) == 0:
            return None
        else:
            return sum(values) / len(values)

    def __str__(self):
        return "%s" % self.number


class Rating(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    view_2d = models.IntegerField(default=0)
    view_3d = models.IntegerField(default=0)
    comment = models.TextField(max_length=200, null=True)
