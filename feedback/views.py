from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import *


# Create your views here.
@login_required
def post_feedback(request):
    if request.method == 'POST':
        username = request.user.username
        title = request.POST.get('title')
        message = request.POST.get('message')
        Feedback.objects.create(user=username, title=title, message=message)
        return redirect('login')
    context = {}
    return render(request, 'feedback_form.html', context)
