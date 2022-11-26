from django.db import models

# Create your models here.

class DowlandFile(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='photo/')
    
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    
    def __str__(self):
        return self.title
