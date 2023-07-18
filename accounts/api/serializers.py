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


class ManagerRegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with password checkup
    """
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = [
            "email", 
            "password",
            "password1",
        ]

    def validate(self, attr):
        attr["is_manager"] = True
        if attr["password"] != attr["password1"]:
            raise serializers.ValidationError({"details": "Passwords does not match"})
        attr.pop("password1")
        return attr

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)