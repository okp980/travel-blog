from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post, Comment, Category, Image
from blog.serializers import (
    PostSerializer,
    CommentSerializer,
    CategorySerializer,
    ImageSerializer,
)
from rest_framework.permissions import IsAuthenticated
from blog.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from drf_spectacular.utils import extend_schema


# Create your views here.
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == "images":
            return ImageSerializer
        if self.action == "comments":
            return CommentSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(
        detail=True,
        methods=[
            "post",
        ],
        parser_classes=[MultiPartParser],
    )
    def images(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        methods=["get"],
    )
    def comments(self, request, *args, **kwargs):
        post = self.get_object()
        comments = post.comments.all().order_by("-created_at")
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
