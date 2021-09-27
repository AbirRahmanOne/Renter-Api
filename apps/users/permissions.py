from rest_framework.permissions import IsAuthenticated

from .models import User


class IsModerator(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        is_moderator = ( request.user.user_type == 'moderator' )
        print(is_moderator)
        return is_authenticated and is_moderator


class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        is_admin = ( request.user.user_type == 'admin' )
        print(is_admin)
        return is_authenticated and is_admin


