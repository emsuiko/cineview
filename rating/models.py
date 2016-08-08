from django.db import models


class Cinema(models.Model):
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
    rating = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.number
