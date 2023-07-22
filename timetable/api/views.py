from timetable.models import Section, FreeSection, SectionTeacher, FreeSectionTeacher
from .serializers import (
    TeacherSectionAdjustSerializer,
    TeacherFreeSectionAdjustSerializer,
    FreeSectionListSerializer,
    SectionListSerializer,
    TeacherListSectionSerializer,
    TeacherListFreeSectionSerializer,
    SetClassSerializer,
    )
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from ..models import Section, FreeSection, iranian_time_slots, chinese_time_slots, DAYS_OF_WEEK
        
class TeacherFreeSectionAdjustAPIView(viewsets.ModelViewSet):
    """
    Gives the list of sections which the requested teacher has.
    """
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
    """
    Adjust  which the requested teacher has.
    """
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
    """
    Gives a list of free sections of a specific teacher
    """
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
    """
    Gives a list of sections of a specific teacher
    """
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
    """
    Gives a list of teachers of a given section
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherListSectionSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        iranian_time = self.kwargs['iranian_time']
        query = SectionTeacher.objects.filter(section__day=day,
                            section__iranian_time=iranian_time ).select_related('teacher')
        return query
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class TeacherListFreeSectionListAPIView(generics.ListAPIView):
    """
    Gives a list of teachers of a given free section
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherListFreeSectionSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        iranian_time = self.kwargs['iranian_time']
        query = FreeSectionTeacher.objects.filter(
            free_section__day=day, 
            free_section__iranian_time=iranian_time
            ).select_related('teacher')
        return query
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
  
class SetClassUpdateAPIView(generics.UpdateAPIView):
    """
    Set an a Student to a teacher in a free section
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SetClassSerializer
    queryset = FreeSectionTeacher.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        teacher = serializer.validated_data.get('teacher')
        free_section = serializer.validated_data.get('free_section')
        free_section_class = serializer.validated_data.get('free_section_class')
        
        try:
            free_section_teacher = self.get_queryset().get(teacher=teacher, free_section=free_section)
        except FreeSectionTeacher.DoesNotExist:
            return Response({'error': 'FreeSectionTeacher not found.'}, status=status.HTTP_404_NOT_FOUND)
        free_section_teacher.free_section_class = free_section_class
        free_section_teacher.save()
        return Response({'message': f'Class "{free_section_class}" has been set .'}, status=status.HTTP_200_OK) 
  
#----------------------------------------Section Creators API---------------------------------------#  
           
class CreateSectionsAPIView(APIView):
    """
    Creates all the of possible sections
    """
    def get(self, request, format=None):
        try:
            Section.objects.all().delete()
            iranian_time_slots = [choice[0] for choice in Section.iranian_time.field.choices]
            chinese_time_slots = [choice[0] for choice in Section.chinese_time.field.choices]
            for day, _ in DAYS_OF_WEEK:
                for i in range(len(iranian_time_slots)):
                    iranian_time = iranian_time_slots[i]
                    chinese_time = chinese_time_slots[i]
                    Section.objects.create(day=day, iranian_time=iranian_time, chinese_time=chinese_time)
            return Response({'message': 'All sections created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f'Error occurred while creating sections: "{e}" '}, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CreateFreeSectionsAPIView(APIView):
    """
    Creates all the of possible free sections
    """
    def get(self, request, format=None):
        try:
            Section.objects.all().delete()
            iranian_time_slots = [choice[0] for choice in FreeSection.iranian_time.field.choices]
            chinese_time_slots = [choice[0] for choice in FreeSection.chinese_time.field.choices]
            for day, _ in DAYS_OF_WEEK:
                for i in range(len(iranian_time_slots)):
                    iranian_time = iranian_time_slots[i]
                    chinese_time = chinese_time_slots[i]
                    FreeSection.objects.create(day=day, iranian_time=iranian_time, chinese_time=chinese_time)
            return Response({'message': 'All free sections created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f'Error occurred while creating free sections: "{e}" '},
                                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        