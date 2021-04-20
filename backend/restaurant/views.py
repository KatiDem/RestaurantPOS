from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.mixins import *


# POST
from user.roles import WaiterRequiredMixin, SuperuserRequiredMixin

from rest_framework.decorators import api_view



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

class TableCreateView(SuperuserRequiredMixin, CreateAPIView):
    """ Create Table """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableListView(ListAPIView, WaiterRequiredMixin):
    """ List Tables """
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableView(UpdateAPIView, WaiterRequiredMixin):
    """ Update Table by name """
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'

class TableDestroyView(DestroyAPIView):
    """ Destroy Table by name """
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'name'




@api_view()
def FullCostOrdersListView(request):
    full_cost = Order.objects.filter(paid=True).aggregate(full_cost=Sum('cost'))
    return Response(full_cost)

@api_view()
def CostTablesListView(request, pk):
    full_cost = Order.objects.filter(table=pk).aggregate(Sum('cost'))
    return Response(full_cost)


@api_view()
def CostYearListView(request, year):
    full_cost = Order.objects.filter(date_of_creation__year=year).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)

@api_view()
def CostMonthListView(request, month):
    full_cost = Order.objects.filter(date_of_creation__month=month).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)

@api_view()
def CostDayListView(request, day):
    full_cost = Order.objects.filter(date_of_creation__day=day).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)