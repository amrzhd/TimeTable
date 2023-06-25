from rest_framework import serializers
from accounts.models import User, Profile


class ManagerRegisterSerializer(serializers.ModelSerializer):
    """Registration serializer with password checkup"""

    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )
    password1 = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )

    class Meta:
        model = User.objects.get(is_manager=True,is_teacher=False)
        fields = [
            "email",
            "password",
            "password1",]
        queryset = User.objects.filter(is_manager=True,is_teacher=False)


    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)
    
class TeacherRegisterSerializer(serializers.ModelSerializer):
    """Registration serializer with password checkup"""

    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )
    password1 = serializers.CharField(
        max_length=68, min_length=6, write_only=True
    )

    class Meta:
        model = User
        fields = ["email", 
                  "password",
                  "password1",]
        queryset = User.objects.filter(is_manager=False,is_teacher=True)

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError(
                {"details": "Passwords does not match"}
            )
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer to manage extra user info"""

    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
        ]
