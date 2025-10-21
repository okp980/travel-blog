from rest_framework import serializers
from blog.models import Post, Comment, Category, Image
from account.serializer import UserSerializer
from django.utils.text import slugify


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image", "created_at"]
        read_only_fields = ["id", "created_at"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    tags = serializers.ListField(
        child=serializers.CharField(max_length=30), required=False
    )
    slug = serializers.SlugField(read_only=True)
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()
    category = CategorySerializer()

    def get_likes(self, obj) -> int:
        return obj.likes.count()

    def get_is_liked_by_user(self, obj) -> bool:
        return obj.likes.filter(id=self.context["request"].user.id).exists()

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["title"])
        return super().create(validated_data)

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()

    def get_likes(self, obj) -> int:
        return obj.likes.count()

    def get_is_liked_by_user(self, obj) -> bool:
        return obj.likes.filter(id=self.context["request"].user.id).exists()

    class Meta:
        model = Comment
        fields = "__all__"
