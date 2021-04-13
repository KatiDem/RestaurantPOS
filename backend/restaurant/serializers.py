
from rest_framework import serializers

from .models import Seating


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = '__all__'


class TableStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = ('id', 'status')