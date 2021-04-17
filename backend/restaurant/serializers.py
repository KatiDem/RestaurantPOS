from .models import *
from rest_framework import serializers



class OrderItemSerializer(serializers.ModelSerializer):
    # menuitem = MenuItemSerializer(many=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'