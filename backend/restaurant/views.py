from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView


class MenuCreateView(CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuUpdateView(UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuListView(ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuDeleteView(DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuRecordView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
