from django.shortcuts import render

from .serializers import *
from .models import *

from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView


class MenuCreateView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer


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
