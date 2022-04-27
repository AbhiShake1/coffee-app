from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest
from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def logout_user(request):
    if request.user is not None:
        logout(request)
    return redirect('login')


def signup_user(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! Your username is {username}')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("rgegergr")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("rgegergr")
            return redirect("home")

        else:
            print("rgegergr")
            messages.info(request, 'Username or Password is incorrect')
            # return render(request, "user/login.html")
    context = {}
    return render(request, "user/login.html", context)
