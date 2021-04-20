from .models import *
from rest_framework import serializers


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(many=True)
    class Meta:
        model = OrderItem
        fields = '__all__'

#class MenuItemSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = MenuItem
   #     fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    table = TableSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields =  ('table', 'number_of_guests', 'items', 'comment')
