from django.contrib import admin

from .models import Location, Cinema, Hall, Row, Seat
import nested_admin

admin.site.register(Location)
admin.site.register(Cinema)


class RowInline(nested_admin.NestedTabularInline):
    model = Row
    extra = 4

    fields = ('number', 'seat_count', )


class HallAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        RowInline
    ]
admin.site.register(Hall, HallAdmin)

admin.site.register(Row)
admin.site.register(Seat)
