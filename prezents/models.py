from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models


class Prezentation(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='photo/')
    video = models.ImageField(upload_to='video/')
    published = models.BooleanField()
