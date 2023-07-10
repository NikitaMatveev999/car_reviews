from rest_framework import permissions


class CommentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        return False
