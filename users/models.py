from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    description = models.TextField()

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
