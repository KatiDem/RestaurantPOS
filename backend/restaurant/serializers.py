from rest_framework import serializers
from .models import Menu, Order, Seating


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'time', 'cooking_instructions', 'purchase_method', 'total_price', 'confirmed',
                  'cancelled', 'ready_delivery', 'delivered', 'delayed', 'paid')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = '__all__'


class TableStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = ('id', 'status')