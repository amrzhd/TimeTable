from timetable.models import Section, FreeSection, SectionTeacher
from .serializers import (
    SectionCreateSerializer,
    FreeSectionCreateSerializer,
    TeacherSectionRegisterSerializer
    )
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from accounts.models import User
from ..models import Section, iranian_time_slots, DAYS_OF_WEEK
        
class TeacherSectionRegisterAPIView(viewsets.ModelViewSet):
    '''
    Gives the list of sections which the requested teacher has.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSectionRegisterSerializer
    
    def get_queryset(self):
        query =  SectionTeacher.objects.filter(user = self.request.user)
        return query
    
    def create(self,request):
        serializer = self.serializer_class(
            data=request.data, many=False, context = {"request" : self.request}
        )
        if serializer.is_valid():    
            try:
                serializer.save()
            except IntegrityError as e:
                return Response(
                    {'message': f'Teacher has been added before {e}'},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
               
class CreateSectionsAPIView(APIView):
    '''
    Creates all the of possible sections
    '''
    def get(self, request, format=None):
        sections_data = []
        for day in DAYS_OF_WEEK:
            for time_slot in iranian_time_slots:
                section_data = {'day': day[0], 'iranian_time': time_slot[0]}
                sections_data.append(section_data)

        serializer = SectionCreateSerializer(data=sections_data, many=True)
        if serializer.is_valid():
            sections = []
            for section_data in serializer.validated_data:
                section = Section.objects.create(
                    day=section_data['day'],
                    iranian_time=section_data['iranian_time'],
                )
                sections.append(section)
            return Response({'message': 'All sections created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CreateFreeSectionsAPIView(APIView):
    '''
    Creates all the of possible free sections
    '''
    def get(self, request, format=None):
        free_sections_data = []
        for day in DAYS_OF_WEEK:
            for time_slot in iranian_time_slots:
                free_section_data = {'day': day[0], 'iranian_time': time_slot[0]}
                free_sections_data.append(free_section_data)

        serializer = FreeSectionCreateSerializer(data=free_sections_data, many=True)
        if serializer.is_valid():
            free_sections = []
            for free_section_data in serializer.validated_data:
                free_section = FreeSection.objects.create(
                    day=free_section_data['day'],
                    iranian_time=free_section_data['iranian_time'],
                )
                free_sections.append(free_section)
            return Response({'message': 'All free sections created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        