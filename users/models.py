from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.shortcuts import resolve_url
# Create your models here.

class User(AbstractUser):
    description = models.TextField()

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return resolve_url('myurl', kwargs={'id': self.id, 'username': self.username})

