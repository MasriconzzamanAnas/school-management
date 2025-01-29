from django.db import models
import os

# Create your models here.

def st_img(instance, filename):
    return os.path.join( 'student_update/media/',instance.name, filename)

class St_img(models.Model):
    COURSE = (
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Computer Science', 'Computer Science'),
        ('Arts', 'Arts'),
        ('Business', 'Business'),
        ('Health', 'Health'),
        ('Others', 'Others')
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(null=True)
    course = models.CharField(max_length=100, choices=COURSE ,null=True)
    image = models.ImageField(upload_to=st_img, null=False)
    checkbox = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

