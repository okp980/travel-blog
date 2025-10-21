from django.shortcuts import render
from rest_framework import generics
from account.serializer import RegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.views import APIView

# Create your views here.


class RootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "docs": reverse("swagger-ui", request=request),
                "auth": {
                    "login": reverse("token_obtain_pair", request=request),
                    "register": reverse("register", request=request),
                },
                "blog": {
                    "posts": reverse("post-list", request=request),
                    "comments": reverse("comment-list", request=request),
                    "categories": reverse("category-list", request=request),
                },
            }
        )


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
