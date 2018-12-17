from user.forms import UserForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from lead.models import Contact

class UserDetail(LoginRequiredMixin, DetailView):
    """
    Show details of the connected user
    """

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        user = User.objects.filter(
            username=self.request.user
        ).values('date_joined', 'last_login')

        try:
            last_contact = Contact.objects.filter(
                user=self.request.user
            ).values(
            ).order_by(
                '-date_joined',
            )[:1].get()

        except ObjectDoesNotExist:
            last_contact = ''

        context = super().get_context_data(**kwargs)
        context.update({
            'last_contact': last_contact,
            'date_joined': user.values_list('date_joined', flat=True).get(),
            'last_login': user.values_list('last_login', flat=True).get(),
        })

        return context


class UserUpdate(LoginRequiredMixin, UpdateView):
    """
    Update user informations
    """
    form_class = UserForm
    success_url = reverse_lazy('user:detail')

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
