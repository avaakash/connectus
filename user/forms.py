from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
 
 #Forms defintions start here
class SignUpForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','sex','school','college','year_of_study','field_of_study','profile_pic']