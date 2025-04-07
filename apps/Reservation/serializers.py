from rest_framework import serializers
from .models import Reservation
from datetime import timedelta
from rest_framework.exceptions import ValidationError


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'table', 'reservation_time', 'duration_minutes']

    def validate(self, data):
        table = data['table']
        reservation_time = data['reservation_time']
        duration_minutes = data['duration_minutes']
        end_time = reservation_time + timedelta(minutes=duration_minutes)

        # Найдём пересекающиеся брони:
        overlapping = Reservation.objects.filter(table=table).exclude(
            pk=self.instance.pk if self.instance else None
        ).filter(
            reservation_time__lt=end_time,
            reservation_time__gte=reservation_time - timedelta(minutes=duration_minutes)
        )

        if overlapping.exists():
            raise ValidationError("Этот столик уже занят в выбранное время.")

        return data
