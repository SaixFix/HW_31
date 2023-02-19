from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPersonalPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return request.user and request.user.is_authenticated and obj == request.user
        else:
            return request.user and request.user.is_authenticated and obj == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
