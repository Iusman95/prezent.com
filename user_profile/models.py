from django.db import models
from users.models import User
# Create your models here.

class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='photo/')
    
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete(save=True)
        super().delete(*args, **kwargs)