from django.contrib import admin
from apps.Reservation.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'reservation_time', 'duration_minutes')
    search_fields = ('customer_name', 'table__name')
    list_filter = ('table',)
    ordering = ['reservation_time']

    def save_model(self, request, obj, form, change):
        obj.clean()
        super().save_model(request, obj, form, change)

admin.site.register(Reservation, ReservationAdmin)