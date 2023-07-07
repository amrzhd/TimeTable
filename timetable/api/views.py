from timetable.models import Section
from .serializers import SectionsListSerializer, TeacherSectionsListSerializer, AddTeachersSerializer, SectionDetailSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from accounts.models import User
from ..models import Section, iranian_time_slots, DAYS_OF_WEEK
    
class SectionsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SectionsListSerializer
    queryset = Section.objects.all()


class AddTeachersToSectionAPIView(generics.UpdateAPIView):
    '''
    Adds a list of teachers to the section which its section id has given in the url pattern.
    '''
    #permission_classes = [IsAuthenticated]
    serializer_class = AddTeachersSerializer
    queryset = Section.objects.all()
    def get_object(self):
        pk = self.kwargs.get('pk')
        section = get_object_or_404(Section, section_id=pk)
        return section
    def update(self, request, *args, **kwargs):
        section = self.get_object()
        serializer = self.get_serializer(section, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        teachers_emails = serializer.validated_data.get('teachers', [])
        for email in teachers_emails:
            teacher = User.objects.filter(email=email, is_teacher=True).first()
            if teacher:
                section.teachers.add(teacher)

        section.save()
        return Response({"message": "Teachers added to the section successfully."}, status=status.HTTP_200_OK)
    
    
class SectionDetailView(generics.RetrieveAPIView):
    '''
    Gives the information about a section by the section id given in the url pattern.
    '''
    #permission_classes = [IsAuthenticated]
    serializer_class = SectionDetailSerializer
    queryset = Section.objects.all()


class TeacherSectionsListAPIView(generics.ListAPIView):
    '''
    Gives the list of sections which the requested teacher has.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherSectionsListSerializer
    def get_queryset(self):
        user = self.request.user
        sections_list =  Section.objects.filter(teachers = user)
        return sections_list
    

# class CreateSectionsAPIView(APIView):
#     def get(self, request, format=None):
#         sections_data = []
#         for day in DAYS_OF_WEEK:
#             for time_slot in iranian_time_slots:
#                 section_data = {'day': day[0], 'iranian_time': time_slot[0]}
#                 sections_data.append(section_data)

#         serializer = SectionSerializer(data=sections_data, many=True)
#         if serializer.is_valid():
#             sections = []
#             for section_data in serializer.validated_data:
#                 section = Section.objects.create(
#                     day=section_data['day'],
#                     iranian_time=section_data['iranian_time'],
#                 )
#                 section.teachers.set([])  # Set teachers as empty list
#                 sections.append(section)
#             return Response({'message': 'All sections created successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)