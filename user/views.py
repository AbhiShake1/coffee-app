from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def signup_user(request: HttpRequest):
    return render(request, "user/signup.html")

