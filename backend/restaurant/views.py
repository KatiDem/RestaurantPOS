from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

class OrderView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'order_number'


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
