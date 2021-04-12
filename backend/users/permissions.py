from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser and request.user.is_active

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser and request.user.is_active


class IsCookUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_cook and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_cook and request.user.is_active


class IsWaiterUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_waiter and request.user.is_active

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_waiter and request.user.is_active


class IsAdminUser(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.is_admin and request.user.is_active

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        return request.user.is_admin and request.user.is_active
