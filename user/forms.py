from django import forms
from .models import User, Post, Comments
from django.contrib.auth.forms import UserCreationForm
 
 #Forms defintions start here
class SignUpForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','sex','school','college','bio','year_of_study','field_of_study']
    
class ProfilePicUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic']

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class NewComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']