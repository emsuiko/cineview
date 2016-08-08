from django.contrib import admin

from .models import Cinema, Hall, Row, Seat

admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Row)
admin.site.register(Seat)
