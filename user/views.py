import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index(request):

    if request.user.is_anonymous:
        return redirect('home')

    template = 'user/index.html'
    user = User.objects.filter(
        username=request.user.username
    ).values('date_joined','last_login')

    context = {
        'date_joined': user.values_list('date_joined', flat=True).get(),
        'last_login': user.values_list('last_login', flat=True).get(),
    }

    return render(request, template, context)
