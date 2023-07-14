from rest_framework import serializers
from accounts.models import User

    
class RegisterSerializer(serializers.ModelSerializer):
    """
    Registration serializer with password checkup
    """
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    password1 = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ["email", 
                  "password",
                  "password1",]

    def validate(self, data):
        if data["password"] != data["password1"]:
            raise serializers.ValidationError({"details": "Passwords does not match"})
        return data

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)

