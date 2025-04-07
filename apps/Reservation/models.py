from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError
from apps.Table.models import Table


class Reservation(models.Model):
    customer_name = models.CharField(
        max_length=100,
        verbose_name="Имя клиента",
        help_text="Введите имя клиента"
    )
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Столик",
        help_text="Выберите столик для брони"
    )
    reservation_time = models.DateTimeField(
        verbose_name="Время бронирования",
        help_text="Укажите время бронирования"
    )
    duration_minutes = models.PositiveIntegerField(
        verbose_name="Продолжительность (в минутах)",
        help_text="Укажите продолжительность бронирования в минутах"
    )

    def clean(self):
        end_time = self.reservation_time + timedelta(minutes=self.duration_minutes)
        overlapping_reservations = Reservation.objects.filter(
            table=self.table
        ).filter(
            models.Q(reservation_time__lt=end_time) & models.Q(reservation_time__gte=self.reservation_time) |
            models.Q(reservation_time__lt=self.reservation_time) & models.Q(reservation_time__gte=end_time)
        )

        if overlapping_reservations.exists():
            raise ValidationError("Этот столик уже занят в выбранное время.")

    def __str__(self):
        return f"Бронь для {self.customer_name} на {self.table.name} с {self.reservation_time}"
