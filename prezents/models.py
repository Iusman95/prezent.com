from django.db import models
from users.models import User

# Create your models here.

class Prezentation(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    user = models.ForeignKey(User, 
                    on_delete=models.CASCADE,
                    verbose_name='Имя пользоваетля')
    description = models.TextField()
    image = models.ImageField(upload_to='photo/')
    video = models.FileField(upload_to='video/')
    published = models.BooleanField()
    evaluation = models.DateTimeField(auto_now=True)
    
    