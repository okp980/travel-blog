from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        AUTHOR = "author", "Author"
        READER = "reader", "Reader"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.READER)

    def __str__(self):
        return self.username
