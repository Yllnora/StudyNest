from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'start_date', 'end_date', 'number_of_people')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('start_date', 'end_date', 'number_of_people')
