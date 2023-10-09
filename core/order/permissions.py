from rest_framework import permissions


class AdultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.id:
            return True
        else:
            if request.user.age <= 18:
                return False
            else:
                return bool(request.user and request.user.is_authenticated)
            

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
