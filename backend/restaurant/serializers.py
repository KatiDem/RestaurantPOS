from rest_framework import serializers
from .models import Order, Menu


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'time', 'cooking_instructions', 'purchase_method', 'total_price', 'confirmed',
                  'cancelled', 'ready_delivery', 'delivered', 'delayed', 'paid')


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name', 'price', 'category', 'comment')