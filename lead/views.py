from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from lead.models import Contact


def index(request):

    if request.user.is_anonymous:
        return redirect('login')

    context = {
        'contacts': 'Pas de contacts',
        'status': False
    }

    contact_dict = Contact.objects.values().filter(user=request.user)

    if contact_dict.count() > 0:
        context.update({
            'contacts': contact_dict,
            'status': True,
        })

    return render(request, 'lead/index.html', context)
