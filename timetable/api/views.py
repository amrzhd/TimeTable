from timetable.models import Section, SectionTeacher, FreeSectionTeacher
from .serializers import (
    TeacherSetFreeSectionSerializer,
    FreeSectionListSerializer,
    SectionListSerializer,
    TeacherListSectionSerializer,
    TeacherListFreeSectionSerializer,
    SetClassSerializer,
    AddFreeSectionsToSectionSerializer,
    ConsultantSetFreeSectionSerializer,
    )
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from ..models import Section, iranian_time_slots, chinese_time_slots, DAYS_OF_WEEK
from .permissions import IsConsultantAuthenticated
        
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TeacherSetFreeSectionSerializer

#---------------------------------Views for Teachers ---------------------------------#

class TeacherSetFreeSectionAPIView(generics.CreateAPIView):
    """
    Teacher sets the free sections
    """
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSetFreeSectionSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, many=False, context={"request": self.request}
        )
        if serializer.is_valid():
            try:
                serializer.save()  # Creates the FreeSectionTeacher instance
                return Response({'message': 'Free section successfully added'})
            except IntegrityError as e:
                return Response(
                    {'error': f'Teacher has been added before {e}'},
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherFreeSectionListAPIView(generics.ListAPIView):
    """
    Gives a list of free sections of a specific teacher (based on teacher id)
    """
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = FreeSectionListSerializer
    def get_queryset(self):
        query = FreeSectionTeacher.objects.all().select_related('free_section')
        return query

    def get(self, request, *args, **kwargs):
            query = self.get_queryset().filter(teacher = request.user)
            serializer = self.serializer_class(query, many=True)
            return Response(serializer.data)

class ConsultantSetFreeSectionAPIView(generics.CreateAPIView):
    """
    Teacher sets the free sections
    """
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = ConsultantSetFreeSectionSerializer
        
    def post(self,request):
        serializer = self.serializer_class(data=request.data, many=False)
        if serializer.is_valid(): 
            try:
                serializer.save()
                return Response({'message':'Free section successfully added'})
            except IntegrityError as e:
                return Response({'error': f'Teacher has been added before {e}'},
                    status=status.HTTP_406_NOT_ACCEPTABLE,)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class FreeSectionListAPIView(generics.ListAPIView):
    """
    Gives a list of free sections of a specific teacher (based on teacher id)
    """
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = FreeSectionListSerializer
    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id'].upper()
        query = FreeSectionTeacher.objects.filter(teacher__teacher_id=teacher_id).select_related('free_section')
        return query

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)  
    
class SectionListAPIView(generics.ListAPIView):
    """
    Gives a list of sections of a specific teacher (based on teacher id)
    """
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = SectionListSerializer
    def get_queryset(self):
        teacher_id = self.kwargs['teacher_id']
        query = SectionTeacher.objects.filter(teacher__teacher_id=teacher_id).select_related('section')
        return query

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class TeacherListSectionListAPIView(generics.ListAPIView):
    """
    Gives a list of teachers of a given section
    """
    permission_classes = [IsConsultantAuthenticated]
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
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = TeacherListFreeSectionSerializer
    
    def get_queryset(self):
        day = self.kwargs['day']
        iranian_time = self.kwargs['iranian_time']
        query = FreeSectionTeacher.objects.filter(free_section__day=day, 
            free_section__iranian_time=iranian_time).select_related('teacher')
        return query
    
    def get(self, request, *args, **kwargs):
        query = self.get_queryset()
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data)
  
class SetClassUpdateAPIView(generics.UpdateAPIView):
    """
    Set an a Student to a teacher in a free section
    """
    permission_classes = [IsConsultantAuthenticated]
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
    
    
class AddFreeSectionsToSectionsCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsConsultantAuthenticated]
    serializer_class = AddFreeSectionsToSectionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.validated_data.get('teacher')
        free_section = serializer.validated_data.get('free_section')
        free_section_class = serializer.validated_data.get('free_section_class')
        
        try:
            free_section_teacher = FreeSectionTeacher.objects.get(
                teacher=teacher, free_section=free_section, free_section_class = free_section_class
            )
        except FreeSectionTeacher.DoesNotExist:
            return Response({'error': 'FreeSectionTeacher not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        teacher = free_section_teacher.teacher
        section = free_section_teacher.free_section
        section_class = free_section_teacher.free_section_class
        SectionTeacher.objects.create(teacher=teacher,section=section, section_class = section_class)
        
        return Response({'message': 'Section has been set.'}, status=status.HTTP_200_OK)
        
        
        
  
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
            FreeSection.objects.all().delete()
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
        