from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_fields'] = Contact.objects.all()

        return context


def edit(request, contact_id):

    if request.user.is_anonymous:
        return redirect('login')

    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    return render(request, "lead/edit.html", {'contact': contact})


def add(request):

    if request.user.is_anonymous:
        return redirect('login')

    return render(request, "lead/add.html", {'form': 'no-form'})
