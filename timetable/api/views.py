from timetable.models import Section
from .serializers import TeacherAssignSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

    
class TeacherAssignListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherAssignSerializer
    queryset = Section.objects.all()
    def perform_create(self, serializer):
        teachers = self.request.data.getlist('teachers[]', [])
        section = serializer.save()
        section.teachers.set(teachers)
    
# class TeacherSetTimeCreateAPIView(generics.CreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TeacherAssignSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class
#         if serializer.is_valid():
#               return self.request
#         return 