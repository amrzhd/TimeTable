from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import (
    ProfileSerializer,
    RegisterSerializer,
)


class RegisterApiView(generics.CreateAPIView):
    """Creates a new user with the given info and credentials"""

    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class ProfileApiView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


