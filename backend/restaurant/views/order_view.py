from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.filters import *
from ..models import Order
from ..serializers import OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDestroyView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
