from .models import *
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        
        
class OrderItemListSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('table', 'number_of_guests', 'items', 'comment')


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('table', 'number_of_guests', 'items', 'comment')
