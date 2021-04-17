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


# GET
class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
