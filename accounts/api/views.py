from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsConsultant, IsSupervisor
from django.shortcuts import get_object_or_404
from accounts.models import User
from .serializers import (
    TeacherRegisterSerializer,
    SupervisorRegisterSerializer,
    ConsultantRegisterSerializer,
    GiveUserIdSerializer,
    UserCheckSerializer,
    )

class UserCheckAPIView(generics.GenericAPIView):
    """
    Checks whether the user is registered before or not
    """
    serializer_class = UserCheckSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            national_code = serializer.validated_data.get('national_code')
            
            # Check if the user with the given national_code exists in the database
            try:
                user = User.objects.get(national_code=national_code)
                return Response({"national_code":f"{national_code}"},
                                status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"message":f"User with national code of {national_code} doesn't exist!"},
                                status=status.HTTP_404_NOT_FOUND)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherRegisterAPIView(generics.GenericAPIView):
    """
    Creates a new teacher user with the given info and credentials
    """

    serializer_class = TeacherRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = TeacherRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Teacher has registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
class SupervisorRegisterAPIView(generics.GenericAPIView):
    """
    Creates a new consultant user with the given info and credentials
    """

    serializer_class = SupervisorRegisterSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = SupervisorRegisterSerializer(data=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"Supervisor has registered successfully"}, status=status.HTTP_201_CREATED)
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
            return Response({"message": f"Consultant has registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GiveUserIdUpdateAPIView(generics.UpdateAPIView):
    """
    Assigns an ID to a teacher
    """
    permission_classes = [IsSupervisor, IsAuthenticated]
    serializer_class = GiveUserIdSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            personal_id = serializer.validated_data.get('personal_id')

            try:
                user = self.get_queryset().get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

            user.personal_id = personal_id
            user.save()

            return Response({'message': 'The id is given to the user successfully!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    