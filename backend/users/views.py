from .serializers import *
from .models.custom_user import *
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
)


class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrievView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDestroyView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AdminCreateView(CreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminListView(ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminRetrievView(RetrieveAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminDestroyView(DestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class =  AdminSerializer
