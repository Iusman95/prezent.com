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
    
    
class Post(models.Model):
    user = models.ForeignKey(User, 
            on_delete=models.CASCADE, 
            verbose_name='пользователь')
    
    file = models.FileField(upload_to='index_file/', verbose_name='файл')
    description = models.TextField(verbose_name='описание файла')



class Comment(models.Model):
    user = models.ForeignKey(User, 
            on_delete=models.CASCADE, 
            verbose_name="пользователь")
        
    post = models.ForeignKey(Post, 
                on_delete=models.CASCADE,
                verbose_name='посты')

    title = models.TextField(verbose_name='описание файла')
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.title



 