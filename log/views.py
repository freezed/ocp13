from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from lead.models import Contact
from log.forms import EntryForm
from log.models import Entry


class EntryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Create a new Entry
    """
    model = Entry
    form_class = EntryForm

    def test_func(self):
        """
        First test to restrict acces to the view
        Checks if the authenticated user owns the requested contact
        Provided by `UserPassesTestMixin`
        https://docs.djangoproject.com/fr/2.1/topics/auth/default/
        """
        return Contact.objects.filter(
            id=self.kwargs['contact_id'],
            user=self.request.user.id,
        ).exists()


    def get_form_kwargs(self):
        """
        Send kwargs to `log.forms.EntryForm` to populate form fields
        with contact & user in a hidden form
        """
        kwargs = super(EntryCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user.id
        kwargs['contact'] = self.kwargs['contact_id']

        return kwargs


    def get_success_url(self, **kwargs):
        """
        Set the success URL,
        I do not find a way to set it on `EntryCreate.success_url` attribute
        """
        return reverse_lazy('lead:view', kwargs={
            'contact_id': self.kwargs['contact_id']
        })



class EntryDetail(LoginRequiredMixin, DetailView):
    """
    Show details of an entry
    """
    model = Entry
    form_class = EntryForm
    pk_url_kwarg = 'entry_id'


    def test_func(self):
        """
        First test to restrict acces to the view
        Checks if the authenticated user owns the requested contact
        Provided by `UserPassesTestMixin`
        https://docs.djangoproject.com/fr/2.1/topics/auth/default/
        """
        return Contact.objects.filter(
            id=self.kwargs['contact_id'],
            user=self.request.user.id,
        ).exists()
