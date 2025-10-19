from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "groups", "user_permissions"]
        read_only_fields = [
            "id",
            "date_joined",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
        ]


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({"error": "Email already exists"})
        if User.objects.filter(username=attrs["username"]).exists():
            raise serializers.ValidationError({"error": "Username already exists"})
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"error": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
