from django.db import models
import os
from django.contrib.auth.models import User
from django.utils import timezone

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
    bio = models.CharField(max_length=244,null=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)

    @property
    def get_comments(self):
        return Comments.objects.filter(post_id=self.id).order_by('-created_at')
    @property
    def get_likes(self):
        return Post_Likes.objects.filter(post_id=self.id).count()
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Post,self).save(*args, **kwargs)

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.CharField(max_length=244)
    created_at = models.DateTimeField(null=True)
    modified_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Comments,self).save(*args, **kwargs)

class Post_Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



