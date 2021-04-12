from rest_framework import viewsets

from users.permissions import IsSuperUser, IsCookUser, IsWaiterUser, IsAdminUser
from users.models import Admin, Cook, Waiter
from users import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = (IsSuperUser | self.user_type_role,)
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = (IsSuperUser,)
        elif self.action == 'destroy':
            permission_classes = (IsSuperUser,)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', ]:
            return self.write_serializer
        return self.read_serializer


class AdminProfileViewSet(UserProfileViewSet):
    queryset = Admin.objects.select_related('user')

    user_type_role = IsAdminUser
    write_serializer = serializers.AdminProfileCreateOrUpdateSerializer
    read_serializer = serializers.AdminProfileSerializer


class CookProfileViewSet(UserProfileViewSet):
    queryset = Cook.objects.select_related('user').prefetch_related('group_set')

    user_type_role = IsCookUser
    write_serializer = serializers.CookProfileCreateOrUpdateSerializer
    read_serializer = serializers.CookProfileSerializer


class WaiterProfileViewSet(UserProfileViewSet):
    queryset = Waiter.objects.select_related('user').prefetch_related('group_set')

    user_type_role = IsWaiterUser
    write_serializer = serializers.WaiterProfileCreateOrUpdateSerializer
    read_serializer = serializers.WaiterProfileSerializer
