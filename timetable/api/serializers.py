
from rest_framework import serializers
from ..models import Section, FreeSection, SectionTeacher
from accounts.models import User

class TeacherSectionRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTeacher
        fields =[
            "free_section",
        ]
    
    def create(self, validated_data):
        validated_data["user"] = self.context.get("request").user

        return super().create(validated_data)
    
class SectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "day",
        ]

class FreeSectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeSection
        fields = [
            "iranian_time",
            "day",
        ]