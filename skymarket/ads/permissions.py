# TODO здесь производится настройка пермишенов для нашего проектa
from rest_framework import permissions


class AdAndCommentPermission(permissions.BasePermission):
    message = 'not allowed'

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.author.id or request.user.role == 'admin':
            return True
        return False
