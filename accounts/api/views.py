from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import (
    TeacherRegisterSerializer,
    ConsultantRegisterSerializer,
    GiveTeacherIdSerializer,
    )

    
class TeacherRegisterAPIView(generics.GenericAPIView):
    """
    Creates a new teacher user with the given info and credentials
    """

    serializer_class = TeacherRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = TeacherRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ConsultantRegisterAPIView(generics.GenericAPIView):
    """
    Creates a new consultant user with the given info and credentials
    """

    serializer_class = ConsultantRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = ConsultantRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GiveTeacherIdUpdateAPIView(generics.UpdateAPIView):
    """
    Assigns an ID to a teacher
    """
    permission_classes = [IsAuthenticated]
    serializer_class = GiveTeacherIdSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        teacher_id = serializer.validated_data.get('teacher_id')

        try:
            user = self.get_queryset().get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)

        user.teacher_id = teacher_id
        user.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    