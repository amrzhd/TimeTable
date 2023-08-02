from rest_framework.permissions import BasePermission

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return super().has_permission(request, view) and user.is_supervisor

class IsConsultant(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return super().has_permission(request, view) and user.is_consultant
       