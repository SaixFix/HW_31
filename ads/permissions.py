from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdPersonalPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return request.user and request.user.is_authenticated and obj.author_id == request.user
        else:
            return request.user and request.user.is_authenticated and obj.author_id == request.user


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class AdModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'moderator'
