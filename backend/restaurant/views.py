from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *


# POST
class OrderItemCreateView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


# PUT,PATCH
class OrderItemUpdateView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# DELETE
class OrderItemDestroyView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class MenuCreateView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

# GET
class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class MenuUpdateView(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class MenuListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class MenuDeleteView(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


class MenuRecordView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

