from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView

from lead.forms import ContactForm
from lead.models import Contact


class ContactList(LoginRequiredMixin, ListView):
    """
    Index page of `lead` app, show contact list of the authenticated user
    """
    model = Contact
    context_object_name = 'contact_list'


class ContactDetail(LoginRequiredMixin, DetailView):
    """
    Show details of the choosen contact
    """
    model = Contact
    pk_url_kwarg = 'contact_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_fields'] = Contact.objects.all()

        return context


class ContactCreate(LoginRequiredMixin, CreateView):
    """
    Create a new Contact
    """
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('lead:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContactUpdate(LoginRequiredMixin, UpdateView):
    """
    Update a contact
    """
    model = Contact
    form_class = ContactForm
    pk_url_kwarg = 'contact_id'
    # success_url = reverse_lazy('lead:view', kwargs={'contact_id': pk_url_kwarg})
    success_url = reverse_lazy('lead:index')


class ContactDelete(LoginRequiredMixin, DeleteView):
    """
    Delete a contact
    """
    model = Contact
    pk_url_kwarg = 'contact_id'
    success_url = reverse_lazy('lead:index')
