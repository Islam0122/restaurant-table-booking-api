import pytest
from rest_framework.exceptions import ValidationError
from datetime import datetime, timedelta
from apps.Table.models import Table
from .models import Reservation
from .serializers import ReservationSerializer
from django.utils import timezone


"""
✅ Логика бронирования:
1.Нельзя создать бронь, если в указанный временной слот столик уже занят (пересечение по времени и table_id).
2.Бронь может длиться произвольное количество минут.
3.Валидации должны обрабатываться на уровне API (например, конфликт брони должен выдавать ошибку с пояснением).
"""

@pytest.mark.django_db
def test_reservation_conflict():
    table = Table.objects.create(name="Table 1", seats=4, location="Main Hall")

    reservation_data_1 = {
        "customer_name": "Иван",
        "table": table,
        "reservation_time": timezone.make_aware(datetime(2025, 4, 1, 10, 0)),
        "duration_minutes": 30
    }
    reservation_1 = Reservation.objects.create(**reservation_data_1)

    reservation_data_2 = {
        "customer_name": "Мария",
        "table": table,
        "reservation_time": timezone.make_aware(datetime(2025, 4, 1, 10, 15)),
        "duration_minutes": 30
    }

    serializer = ReservationSerializer(data={
        "customer_name": reservation_data_2["customer_name"],
        "table": table.id,  # передаём id
        "reservation_time": reservation_data_2["reservation_time"].isoformat(),
        "duration_minutes": reservation_data_2["duration_minutes"],
    })

    assert not serializer.is_valid()
    assert "Этот столик уже занят" in str(serializer.errors)
