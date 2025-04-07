from django.db import models
from django.db.models import Q

class Table(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Название столика",
        help_text="Уникальное имя столика, например, 'Table 1'"
    )
    seats = models.PositiveSmallIntegerField(
        verbose_name="Количество мест",
        help_text="Введите количество посадочных мест за столиком"
    )
    location = models.CharField(
        max_length=100,
        verbose_name="Расположение",
        help_text="Например, 'зал у окна' или 'терраса'"
    )

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"
        ordering = ['name']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(seats__gte=1),
                name="min_seats_check"
            )
        ]

    def __str__(self):
        return f"{self.name} – {self.seats} мест ({self.location})"
