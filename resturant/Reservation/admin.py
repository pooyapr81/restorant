from django.contrib import admin
from .models import Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'date', 'time', 'phone')
    search_fields = ('name', 'phone', 'number', 'date', 'time')
    list_filter = ('date', 'time', 'number')


admin.site.register(Reservation, ReservationAdmin)
