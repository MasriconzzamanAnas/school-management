from . import models
from django import forms

class st_gelary(forms.ModelForm):
    class Meta:
        model = models.St_img
        fields = ['name','email','phone','course','image','checkbox']
        lable ={
            'name': "Your full name",
            'email': 'fullname@example.com',
            'phone': 'your Phone Number',
            'course': 'select course', 
            'image' : "upload your photo",
            'checkbox':'completed'
        }
        help_text ={
            "image": "your photo will show in photo gallery"
        }


# <!-- Name, Email, Phone Number, Course. -->