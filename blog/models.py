from django.db import models
from account.models import User

# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT
    )
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="post_category"
    )
    tags = models.JSONField(default=list, blank=True)
    likes = models.ManyToManyField(User, related_name="liked_posts")
    place_visited = models.CharField(max_length=200)
    date_visited = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    likes = models.ManyToManyField(User, related_name="liked_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
