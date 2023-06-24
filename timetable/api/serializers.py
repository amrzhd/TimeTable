
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

class TeacherAssignSerializer(serializers.ModelSerializer):
    #teacher = serializers.SerializerMethodField(read_only=False)
    teachers = TeacherSerializer(many=True)
    class Meta:
        model = Section
        fields = [
            "iranian_time",
            "chinese_time",
            "day",
            "teachers",
        ]
        # def create(self, validated_data):
        #     tracks_data = validated_data.pop('tracks')
            # album = Album.objects.create(**validated_data)
            # for track_data in tracks_data:
            # Track.objects.create(album=album, **track_data)
            # return album
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["teachers"] = [teacher.email for teacher in instance.teachers.all()]
        return rep

        #for 1 teacher per section:
        # rep = super().to_representation(instance)
        # rep["teacher"] = instance.teacher.email
        # return rep
    
    