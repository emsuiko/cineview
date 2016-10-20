from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Location(MPTTModel):
    city = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def get_absolute_url(self):
        return '/rating/location/%i' % self.pk

    def breadcrumbs(self):
        return []

    def __str__(self):
        return "%s" % self.city


class Cinema(MPTTModel):
    parent = TreeForeignKey(Location, on_delete=models.CASCADE, related_name='cinema', verbose_name='Location')
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return self.parent.get_absolute_url() + '/cinema/%i' % self.pk

    def breadcrumbs(self):
        return [self.parent]

    def __str__(self):
        return "%s" % self.name


class Hall(MPTTModel):
    parent = TreeForeignKey(Cinema, on_delete=models.CASCADE, related_name='halls', verbose_name='Cinema')
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return self.parent.get_absolute_url() + '/hall/%i/view/2' % self.pk

    def breadcrumbs(self):
        return [self.parent.parent, self.parent]

    def __str__(self):
        return "%s" % self.name


class Row(MPTTModel):
    parent = TreeForeignKey(Hall, on_delete=models.CASCADE, related_name='rows', verbose_name='Hall')
    number = models.CharField(max_length=10)
    seat_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Row, self).save(*args, **kwargs)

        old_seat_count = len(self.seats.all())
        diff = self.seat_count - old_seat_count

        start = 1
        if diff > 0:
            start = old_seat_count+1

        for i in range(start, self.seat_count+1):
                seat = Seat()
                seat.parent = self
                seat.number = i
                seat.save()

    def __str__(self):
        return "%s" % self.number


class Seat(MPTTModel):
    parent = TreeForeignKey(Row, on_delete=models.CASCADE, related_name='seats', verbose_name='Row')
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

    def ratings(self):
        return self.rating_set.all()

    def get_absolute_url(self):
        return self.parent.parent.get_absolute_url() + '/seat/%i' % self.pk

    def breadcrumbs(self):
        return [self.parent.parent.parent.parent, self.parent.parent.parent, self.parent.parent]

    def __str__(self):
        return "%s" % self.number


class Rating(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    view_2d = models.IntegerField(default=0)
    view_3d = models.IntegerField(default=0)
    comment = models.TextField(max_length=200, null=True)
