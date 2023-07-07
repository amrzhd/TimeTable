
from rest_framework import serializers
from ..models import Section
from accounts.models import User

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
        ]
        
class SectionDetailSerializer(serializers.ModelSerializer):
    section_id = serializers.IntegerField(read_only=True)
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Section
        fields = [
            "section_id",
            "iranian_time",
            "day",
            "teachers",
        ]

class SectionsListSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Section
        fields = [
            "section_id",
            "iranian_time",
            "day",
            "teachers",
        ]        

class AddTeachersSerializer(serializers.ModelSerializer):
    teachers = serializers.ListField(child=serializers.EmailField())

    class Meta:
        model = Section
        fields = ['teachers']

    def validate(self, attrs):
        teachers_emails = attrs.get('teachers', [])
        return attrs

    def update(self, instance, validated_data):
        teachers_emails = validated_data.get('teachers', [])
        return instance

class TeacherSectionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "day",
        ]
        
# class SectionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Section
#         exclude = ["teachers"]


    