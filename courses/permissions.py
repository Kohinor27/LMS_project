from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Teacher').exists()

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Student').exists()

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
