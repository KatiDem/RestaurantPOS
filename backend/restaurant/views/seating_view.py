from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from ..serializers import TableStatusSerializer, TableSerializer
from ..models import Seating


class TableListView(ListAPIView):
    queryset = Seating.objects.all()
    serializer_class = TableSerializer


class TableFreeListView(ListAPIView):
    queryset = Seating.objects.filter(status=False)
    serializer_class = TableSerializer


class TableCreateView(CreateAPIView):
    queryset = Seating.objects.all()
    serializer_class = TableSerializer


class TableDeleteView(DestroyAPIView):
    queryset = Seating.objects.all()
    serializer_class = TableSerializer


class TableStatusPatchView(UpdateAPIView):
    queryset = Seating.objects.all()
    serializer_class = TableStatusSerializer