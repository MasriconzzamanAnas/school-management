# Generated by Django 5.1.5 on 2025-01-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_update', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='st_img',
            name='Class',
        ),
        migrations.AddField(
            model_name='st_img',
            name='course',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='st_img',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
