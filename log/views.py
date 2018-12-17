# from lead.models import Contact
# from log.models import Entry
# from log.forms import EntryForm

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# from django.shortcuts import get_object_or_404
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView


class EntryCreate(LoginRequiredMixin, CreateView):
    """
    Create a new Entry
    """
    # model = Entry
    # form_class = EntryForm
    # success_url = reverse_lazy('lead:view', contact_id)

    # def form_valid(self, form):
        # form.instance.user = self.request.user
        # return super().form_valid(form)
    pass


class EntryDetail(LoginRequiredMixin, DetailView):
    """
    Show details of an entry
    """
    pass


class EntryUpdate(LoginRequiredMixin, UpdateView):
    """
    Update un entry
    """
    pass
