from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class User(AbstractUser):
    mail = models.EmailField(max_length=200, verbose_name='mail')
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
