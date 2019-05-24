"""connectus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from user import views as acc_views
from django.urls import path
from django.views.static import serve
from django.conf import settings    

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^signup/$', acc_views.signup, name='signup'),
    url(r'^logout/$', LogoutView.as_view(),name='logout'),
    url(r'^$', acc_views.home, name='home'),
    url(r'^(?P<username>\w+)/(?P<pk>\d+)/$', acc_views.profile, name='profile'),
    url(r'^(?P<username>\w+)/(?P<pk>\d+)/about/$', acc_views.about, name='about'),
    url(r'^(?P<username>\w+)/(?P<pk>\d+)/about/edit/$', acc_views.about_edit, name='about_edit'),
    url(r'^(?P<username>\w+)/(?P<pk>\d+)/profile_pic/$', acc_views.update_profile_pic, name='update_profile_pic'),
    url(r'^(?P<username>\w+)/(?P<pk>\d+)/friends/$', acc_views.friend_list, name='friend_list'),
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),    
    
]
