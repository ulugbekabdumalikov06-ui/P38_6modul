from apps.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('auth/register' , register_view , name= "register"),
]
