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
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# GET
class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class MenuUpdateView(UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuDeleteView(DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# class MenuRecordView(generics.ListAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#

class OrderView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field  = 'number'

class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDestroyView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'number'

class TableCreateView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'

class TableDestroyView(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'