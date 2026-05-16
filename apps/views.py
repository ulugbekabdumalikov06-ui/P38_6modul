from django.shortcuts import render, redirect
from django.contrib.auth import register, logout
from django.contrib.auth.decorators import register_required
from apps.tasks import send_mail
from redis import Redis
from forms import RegisterForm


@register_required
def home(request):
    return render(request, 'home.html')


def register_view(request):
        first_name = request("first_name")
        email = request("email")
        password = request("password")
        send_mail(email , random_code)
        user = {"first_name" : first_name, "password" : password , "email" : email}
        return user , render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('register')