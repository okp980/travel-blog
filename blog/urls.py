from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostView, CommentView, CategoryView

router = DefaultRouter()
router.register(r"posts", PostView, basename="post")
router.register(r"comments", CommentView, basename="comment")
router.register(r"categories", CategoryView, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
