from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from lead.models import Contact


def index(request):

    if request.user.is_anonymous:
        return redirect('login')

    label_list = [
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'organization',
        'date_joined',
        'date_edit',
    ]

    context = {
        'contacts': 'Pas de contacts',
        'status': False
    }

    contact_dict = Contact.objects.values(*label_list).filter(user=request.user)

    if contact_dict.count() > 0:
        context.update({
            'contacts': contact_dict,
            'status': True,
            'label_list': label_list,
        })

    return render(request, 'lead/index.html', context)


def edit(request, contact_id):

    if request.user.is_anonymous:
        return redirect('login')

    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    return render(request, "lead/edit.html", {'contact': contact})


def view(request, contact_id):

    if request.user.is_anonymous:
        return redirect('login')

    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    return render(request, "lead/view.html", {'contact': contact})


def add(request):

    if request.user.is_anonymous:
        return redirect('login')

    return render(request, "lead/add.html", {'form': 'no-form'})
