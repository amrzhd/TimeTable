from rest_framework import serializers
from accounts.models import User

    
class TeacherRegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with password checkup
    """
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "national_code",
            "first_name",
            "last_name",
            "password",
            "password1",
        ]

    def validate(self, attr):
        attr["is_teacher"] = True
        if attr["password"] != attr["password1"]:
            raise serializers.ValidationError({"details": "Passwords does not match"})
        attr.pop("password1")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class SupervisorRegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with password checkup
    """
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "national_code",
            "first_name",
            "last_name",
            "password",
            "password1",
        ]

    def validate(self, attr):
        attr["is_supervisor"] = True
        if attr["password"] != attr["password1"]:
            raise serializers.ValidationError({"details": "Passwords does not match"})
        attr.pop("password1")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ConsultantRegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with password checkup
    """
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "national_code",
            "first_name",
            "last_name",
            "password",
            "password1",
        ]

    def validate(self, attr):
        attr["is_consultant"] = True
        if attr["password"] != attr["password1"]:
            raise serializers.ValidationError({"details": "Passwords does not match"})
        attr.pop("password1")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class GiveTeacherIdSerializer(serializers.Serializer):
    email = serializers.EmailField()
    teacher_id = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        instance.teacher_id = validated_data['teacher_id']
        instance.save()
        return instance