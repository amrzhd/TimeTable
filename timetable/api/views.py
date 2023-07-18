from timetable.models import Section, FreeSection, SectionTeacher, FreeSectionTeacher
from .serializers import (
    SectionCreateSerializer,
    FreeSectionCreateSerializer,
    TeacherSectionAdjustSerializer,
    TeacherFreeSectionAdjustSerializer,
    FreeSectionListSerializer,
    SectionListSerializer,
    TeacherListSectionSerializer,
    TeacherListFreeSectionSerializer,
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
        
class TeacherFreeSectionAdjustAPIView(viewsets.ModelViewSet):
    '''
    Gives the list of sections which the requested teacher has.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherFreeSectionAdjustSerializer
    
    def get_queryset(self):
        query =  FreeSectionTeacher.objects.filter(user = self.request.user)
        return query
    
    def create(self,request):
        serializer = self.serializer_class(
            data=request.data, many=False, context = {"request" : self.request}
        )
        if serializer.is_valid():    
            try:
                serializer.save()
                return Response(
                    {'message':'Free section successfully added'}
                )
            except IntegrityError as e:
                return Response(
                    {'message': f'Teacher has been added before {e}'},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, *args, **kwargs):
          # Get the requested user
        
        serializer = self.serializer_class(
            data=request.data, many=False, context={"request": self.request}
        )

        if serializer.is_valid():
            free_section = serializer.validated_data.get("free_section")
            section_teacher = SectionTeacher.objects.get(
                user=request.user, free_section=free_section
            )

            if section_teacher:
                section_teacher.free_section.delete()  # Delete the free section

                return Response(
                    {"detail": "Free section successfully deleted"},
                    status=status.HTTP_204_NO_CONTENT,
                )

        return Response(
            {"detail": "Free section not found or you don't have permission to delete"},
            status=status.HTTP_404_NOT_FOUND,
        )
        
class TeacherSectionAdjustAPIView(viewsets.ModelViewSet):
    '''
    Assigns  which the requested teacher has.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSectionAdjustSerializer
    
    def get_queryset(self):
        query =  SectionTeacher.objects.filter(user = self.request.user)
        return query
    
    def create(self,request):
        serializer = self.serializer_class(
            data=request.data, many=False
        )
        if serializer.is_valid():    
            try:
                serializer.save()
                return Response(
                    {'message':'Teacher added successfully to the section'}
                )
            except IntegrityError as e:
                return Response(
                    {'message': f'Teacher has been added before {e}'},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FreeSectionListAPIView(generics.ListAPIView):
    '''
    Gives a list of free sections of a specific teacher
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = FreeSectionListSerializer
    def get_queryset(self):
        user_email = self.kwargs['teacher_email']
        query = FreeSectionTeacher.objects.filter(teacher__email=user_email).select_related('free_section')
        return query

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)    
    
class SectionListAPIView(generics.ListAPIView):
    '''
    Gives a list of sections of a specific teacher
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = SectionListSerializer
    def get_queryset(self):
        user_email = self.kwargs['teacher_email']
        query = SectionTeacher.objects.filter(teacher__email=user_email).select_related('section')
        return query

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class TeacherListSectionListAPIView(generics.ListAPIView):
    '''
    Gives a list of teachers of a given section
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherListSectionSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        iranian_time = self.kwargs['iranian_time']
        query = SectionTeacher.objects.filter(section__day=day, section__iranian_time=iranian_time ).select_related('teacher')
        return query
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class TeacherListFreeSectionListAPIView(generics.ListAPIView):
    '''
    Gives a list of teachers of a given section
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherListFreeSectionSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        iranian_time = self.kwargs['iranian_time']
        query = FreeSectionTeacher.objects.filter(free_section__day=day, free_section__iranian_time=iranian_time ).select_related('teacher')
        return query
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
             
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
        