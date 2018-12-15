from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from lead.models import Contact


class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contact_list'


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
