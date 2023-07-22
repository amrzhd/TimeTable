
from rest_framework import serializers
from ..models import Section, FreeSection, SectionTeacher, FreeSectionTeacher
# from accounts.models import User

class TeacherFreeSectionAdjustSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "free_section",
        ]
    
    def create(self, validated_data):
        validated_data["teacher"] = self.context.get("request").user
        return super().create(validated_data)
    
class TeacherSectionAdjustSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTeacher
        fields =[
            "chinese_time",
            "teacher",
            "section",
        ]
        
class SectionListSerializer(serializers.ModelSerializer):
    iranian_time = serializers.CharField(source='section.iranian_time')
    chinese_time = serializers.CharField(source='section.chinese_time')
    day = serializers.CharField(source='section.day')
    class Meta:
        model = SectionTeacher
        fields = [
            "chinese_time",
            "iranian_time", 
            "day",
        ]

class FreeSectionListSerializer(serializers.ModelSerializer):
    iranian_time = serializers.CharField(source='free_section.iranian_time')
    chinese_time = serializers.CharField(source='free_section.chinese_time')
    day = serializers.CharField(source='free_section.day')
    class Meta:
        model = FreeSectionTeacher
        fields = [
            "chinese_time",
            "iranian_time", 
            "day",
        ]
    
class TeacherListSectionSerializer(serializers.ModelSerializer):
    teacher_email = serializers.CharField(source='teacher.email')
    class Meta:
        model = SectionTeacher
        fields = [
            "teacher_email",
        ]
    
class TeacherListFreeSectionSerializer(serializers.ModelSerializer):
    teacher_email = serializers.CharField(source='teacher.email')
    class Meta:
        model = FreeSectionTeacher
        fields = [
            "teacher_email",
        ]    
    