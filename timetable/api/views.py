from timetable.models import Section
from .serializers import TeacherAssignSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

    
class TeacherAssignModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TeacherAssignSerializer
    queryset = Section.objects.all()