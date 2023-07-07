from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import (
    ManagerRegisterSerializer,
    TeacherRegisterSerializer,
)

    
class TeacherRegisterApiView(generics.CreateAPIView):
    """Creates a new teacher user with the given info and credentials"""

    serializer_class = TeacherRegisterSerializer
    queryset = User.objects.filter(is_teacher=True)

class ManagerRegisterApiView(generics.CreateAPIView):
    """Creates a new manager user with the given info and credentials"""
    
    serializer_class = ManagerRegisterSerializer
    queryset = User.objects.filter(is_manager=True)


