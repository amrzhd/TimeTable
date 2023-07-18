from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import TeacherRegisterSerializer, ManagerRegisterSerializer

    
class TeacherRegisterAPIView(generics.GenericAPIView):
    """Creates a new teacher user with the given info and credentials"""

    serializer_class = TeacherRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = TeacherRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ManagerRegisterAPIView(generics.GenericAPIView):
    """Creates a new teacher user with the given info and credentials"""

    serializer_class = ManagerRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = ManagerRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
