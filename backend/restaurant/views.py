from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *


# POST
class OrderItemCreateView(CreateAPIView):
    """ Create order item """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer


# PUT,PATCH
class OrderItemUpdateView(UpdateAPIView):
    """ Update order item by """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemCreateSerializer


# DELETE
class OrderItemDestroyView(DestroyAPIView):
    """ Delete order item by """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer


class MenuCreateView(CreateAPIView):
    """ Create Menu item """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# GET
class OrderItemListView(ListAPIView):
    """ List Order item """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer


class MenuUpdateView(UpdateAPIView):
    """ Update Menu item """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListView(ListAPIView):
    """ List Menu items """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuDeleteView(DestroyAPIView):
    """ Delete Menu item """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# class MenuRecordView(generics.ListAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#

class OrderView(UpdateAPIView):
    """ Update Order by number """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    lookup_field = 'number'

class OrderListView(ListAPIView):
    """ List Order """
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class OrderCreateView(CreateAPIView):
    """ Create Order """
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer

class OrderDestroyView(DestroyAPIView):
    """ Delete Order by number """
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_field = 'number'

class TableCreateView(CreateAPIView):
    """ Create Table """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableListView(ListAPIView):
    """ List Tables """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableView(UpdateAPIView):
    """ Update Table by name """
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'

class TableDestroyView(DestroyAPIView):
    """ Destroy Table by name """
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'
