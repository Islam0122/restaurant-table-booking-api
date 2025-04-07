from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name', 'seats', 'location']
        read_only_fields = ['id']

    def validate_seats(self, value):
        if value < 1:
            raise serializers.ValidationError("Количество мест должно быть больше нуля.")
        return value
