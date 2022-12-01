# Generated by Django 4.1.3 on 2022-11-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prezents', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to='index_file/', verbose_name='файл'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='image_index_file/', verbose_name='фотографии'),
        ),
    ]