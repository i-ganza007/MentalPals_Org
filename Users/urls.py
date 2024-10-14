from django.urls import path , include 
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile')   
]