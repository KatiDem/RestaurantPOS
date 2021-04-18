from django.shortcuts import render


from .serializers import *
from .models import *
from rest_framework.generics import *

from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

@api_view()
def FullCostOrdersListView(request):
    full_cost = Order.objects.filter(paid=True).aggregate(full_cost=Sum('cost'))
    return Response(full_cost)

@api_view()
def CostTablesListView(request, pk):
    full_cost = Order.objects.filter(table=pk).aggregate(Sum('cost'))
    return Response(full_cost)


@api_view()
def CostTablesYearListView(request, year):
    full_cost = Order.objects.filter(date_of_creation__year=year).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)

@api_view()
def CostTablesMonthListView(request, month):
    full_cost = Order.objects.filter(date_of_creation__month=month).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)

@api_view()
def CostTablesDayListView(request, day):
    full_cost = Order.objects.filter(date_of_creation__day=day).exclude(paid=False).aggregate(full_cost=Sum('cost'))

    return Response(full_cost)