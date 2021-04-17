from .models import *
from rest_framework import serializers



class OrderItemSerializer(serializers.ModelSerializer):
    # menuitem = MenuItemSerializer(many=True)
    class Meta:
        model = OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
