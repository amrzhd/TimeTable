
from rest_framework import serializers
from ..models import Section

class TeacherAssignSerializer(serializers.ModelSerializer):
    teacher = serializers.ModelSerializer(Section.teacher)
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "chinese_time",
            "day",
        ]