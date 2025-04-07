import pytest
from django.core.exceptions import ValidationError
from apps.Table.models import Table

"""
✅ Условия:
Тестируем, что:
1. Столик создаётся корректно.
2. Нельзя создать столик с 0 мест.
3. Уникальность имени работает.
"""


@pytest.mark.django_db
def test_create_table_success():
    table = Table.objects.create(
        name="Table A",
        seats=4,
        location="Зал у окна"
    )
    assert table.name == "Table A"
    assert table.seats == 4
    assert table.location == "Зал у окна"
    assert str(table) == "Table A – 4 мест (Зал у окна)"


@pytest.mark.django_db
def test_table_seats_must_be_positive():
    table = Table(name="Table B", seats=0, location="Терраса")
    with pytest.raises(ValidationError):
        table.full_clean()


@pytest.mark.django_db
def test_table_name_must_be_unique():
    Table.objects.create(name="Table C", seats=2, location="Зал")
    table = Table(name="Table C", seats=3, location="Терраса")
    with pytest.raises(ValidationError):
        table.full_clean()

