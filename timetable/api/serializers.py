
from rest_framework import serializers
from ..models import Section, SectionTeacher, FreeSectionTeacher, Class
from accounts.models import User

class TeacherSetFreeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "section",
        ]
        
    def create(self, validated_data):
        validated_data["teacher"] = self.context.get("request").user
        return super().create(validated_data)
    
        
class SupervisorSetFreeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields =[
            "section",
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
    section__chinese_time = serializers.SerializerMethodField()
    section__iranian_time = serializers.SerializerMethodField()
    section__day = serializers.SerializerMethodField()
    section__month = serializers.SerializerMethodField()
    section__year = serializers.SerializerMethodField()
    
    class Meta:
        model = SectionTeacher
        fields = [
            "section__chinese_time",
            "section__iranian_time", 
            "section__day",
            "section__month",
            "section__year",
            "section_class",
        ]

    def get_section__chinese_time(self, obj):
        return obj.section.chinese_time

    def get_section__iranian_time(self, obj):
        return obj.section.iranian_time

    def get_section__day(self, obj):
        return obj.section.day

    def get_section__month(self, obj):
        return obj.section.month
    
    def get_section__year(self, obj):
        return obj.section.year

class AddFreeSectionsToSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSectionTeacher
        fields = [
            "teacher",
            "section",
            "section_class",
        ]

class FreeSectionListSerializer(serializers.ModelSerializer):
    section__chinese_time = serializers.SerializerMethodField()
    section__iranian_time = serializers.SerializerMethodField()
    section__day = serializers.SerializerMethodField()
    section__month = serializers.SerializerMethodField()
    section__year = serializers.SerializerMethodField()
    
    class Meta:
        model = FreeSectionTeacher
        fields = [
            "section__chinese_time",
            "section__iranian_time", 
            "section__day",
            "section__month",
            "section__year",
            "section_class",
        ]

    def get_section__chinese_time(self, obj):
        return obj.section.chinese_time

    def get_section__iranian_time(self, obj):
        return obj.section.iranian_time

    def get_section__day(self, obj):
        return obj.section.day

    def get_section__month(self, obj):
        return obj.section.month
    
    def get_section__year(self, obj):
        return obj.section.year
    
    
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
            "section",
            "section_class",
        ]
    