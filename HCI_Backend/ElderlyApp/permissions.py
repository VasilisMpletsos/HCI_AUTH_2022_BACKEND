from rest_framework import permissions

class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
             return False
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj == request.user