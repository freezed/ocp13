from user.forms import UserForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView


class UserDetail(LoginRequiredMixin, DetailView):
    """
    Show details of the connected user
    """

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        user = User.objects.filter(
            username=self.request.user
        ).values('date_joined', 'last_login')

        context = super().get_context_data(**kwargs)
        context['date_joined'] = user.values_list(
            'date_joined', flat=True
        ).get()
        context['last_login'] = user.values_list(
            'last_login', flat=True
        ).get()

        return context


class UserUpdate(LoginRequiredMixin, UpdateView):
    """
    Update user informations
    """
    form_class = UserForm
    success_url = reverse_lazy('user:detail')

    def get_object(self):
        return get_object_or_404(User, pk=self.request.username.id)
