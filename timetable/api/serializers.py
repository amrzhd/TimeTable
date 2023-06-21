
from rest_framework import serializers
from ..models import Section
from accounts.models import User

class TeacherAssignSerializer(serializers.ModelSerializer):
    #teacher = serializers.SerializerMethodField(read_only=False)
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_teacher=True))
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "chinese_time",
            "day",
            "teacher",
        ]
        
    # def get_teacher(self, obj):
    #     teacher = obj.teacher
    #     if teacher.is_teacher:
    #         return teacher.email
    #     else:
    #         return None
    