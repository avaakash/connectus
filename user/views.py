from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import SignUpForm, ProfileUpdate
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

@login_required
def home(request):
    return render(request,'home.html',{'user':request.user})

def profile(request,username,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'profile.html', {'user':user})

def about(request, username, pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'about.html',{'user':user})

def about_edit(request, username, pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = ProfileUpdate(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('about', username=user.username, pk=user.pk)
    else:
        form = ProfileUpdate()
    return render(request,'about_edit.html',{'form':form})

def friend_list(request,username,pk):
    user = get_object_or_404(User,username=username,pk=pk)
    return render(request,'friend_list.html',{'user':user})