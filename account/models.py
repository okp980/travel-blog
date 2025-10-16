from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username
