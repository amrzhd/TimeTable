
from rest_framework import serializers
from ..models import Section
from accounts.models import User

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "is_teacher",
            "is_manager",
        ]
        queryset = User.objects.filter(is_manager=True,is_teacher=False)


class TeacherAssignSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "chinese_time",
            "day",
            "teachers",
        ]        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["teachers"] = [teacher.email for teacher in instance.teachers.all()]
        return rep
    
    