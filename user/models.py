from django.db import models
import os
from django.contrib.auth.models import User

# Create your models here.
def get_image_path(instance,filename):
    return os.path.join('user/profile_images', str(instance.pk),filename)

def default_image():
    return os.path.join('static/img/', 'default_profile.svg')

class User(User):
    dob = models.DateField(null=True)
    SEX = (('M','Male'),('F','Female'))
    sex = models.CharField(max_length=1,choices=SEX,null=True)
    profile_pic = models.ImageField(upload_to=get_image_path,default=default_image)
    school = models.CharField(max_length=150,null=True)
    college = models.CharField(max_length=150,null=True)
    year_of_study = models.PositiveIntegerField(null=True)
    field_of_study = models.CharField(max_length=100,null=True)

