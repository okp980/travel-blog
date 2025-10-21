from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
