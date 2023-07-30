
from rest_framework import serializers
from ..models import Section, SectionTeacher, FreeSectionTeacher, Class
from accounts.models import User

class TeacherSetFreeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "free_section",
        ]
        
    def create(self, validated_data):
        validated_data["teacher"] = self.context.get("request").user
        return super().create(validated_data)
    
        
class ConsultantSetFreeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "free_section",
            "teacher",
        ]
            
    
class TeacherSectionAdjustSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTeacher
        fields =[
            "teacher",
            "section",
        ]
        
class SectionListSerializer(serializers.ModelSerializer):
    iranian_time = serializers.CharField(source='section.iranian_time')
    chinese_time = serializers.CharField(source='section.chinese_time')
    day = serializers.CharField(source='section.day')
    #section_class = serializers.CharField(source='teacher.email')

    class Meta:
        model = SectionTeacher
        fields = [
            "chinese_time",
            "iranian_time", 
            "day",
            "section_class",
        ]

class AddFreeSectionsToSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields = [
            "teacher",
            "free_section",
            "free_section_class",
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
        
class SetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "teacher",
            "free_section",
            "free_section_class",
        ]
    