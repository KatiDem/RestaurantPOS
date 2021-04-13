from rest_framework import generics
from rest_framework.generics import (
    CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
)
from ..models import Menu
from ..serializers import MenuSerializer


class MenuCreateView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuUpdateView(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuListView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDeleteView(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuRecordView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer