from rest_framework.permissions import BasePermission

class IsConsultantAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return super().has_permission(request, view) and user.is_consultant