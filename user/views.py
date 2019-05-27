from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Post, Comments, Post_Likes
from .forms import SignUpForm, ProfileUpdate, ProfilePicUpdate, NewPost, NewComment
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
# Create your views here.

@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

@login_required
def home(request):
    return render(request,'home.html',{'user':request.user})

def profile(request,username,pk):
    user = get_object_or_404(User,pk=pk)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('profile',username,pk)
    else:
        form = NewPost()
    return render(request,'profile.html', {'user':user,'form':form,'posts':posts, })

def about(request, username, pk):
    user = get_object_or_404(User,pk=pk)
    if request.user.pk == user.pk:
        if request.method == 'POST':
            form = ProfileUpdate(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('about', username=user.username, pk=user.pk)
        else:
            form = ProfileUpdate(instance=user)
        return render(request,'about.html',{'form':form,'user':user})
    else:
        return render(request,'about.html',{'user':user})


def friend_list(request,username,pk):
    user = get_object_or_404(User,username=username,pk=pk)
    return render(request,'friend_list.html',{'user':user})

def update_profile_pic(request,username,pk):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.user.pk == int(pk):
        if request.method == 'POST':
            form = ProfilePicUpdate(request.POST, request.FILES, instance=user)
            if form.is_valid:
                form.save()
                return redirect('profile', username, pk)
        else:
            form = ProfilePicUpdate()
        return render(request,'update_profile_pic.html', {'form':form, 'user':user})
    else:
        return redirect('profile',user.username,user.pk )

def post_comment(request,username,pk,post_pk):
    user = get_object_or_404(User,pk=request.user.pk)
    post = get_object_or_404(Post,pk=post_pk)
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.save()
            return redirect('post_comment', username,pk,post_pk)
    else:
        form = NewComment()
    return render(request,'post_comment.html',{'form':form,'post':post,'user':get_object_or_404(User,pk=pk)})

def post_likes(request,username,pk,post_pk):
    user = get_object_or_404(User,pk=request.user.pk)
    newlike = Post_Likes.objects.get_or_create(user=user, post_id=post_pk)
    return redirect('profile',username,pk)