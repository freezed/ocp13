import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lead.models import Contact


class Entry(models.Model):
    """
    Class implementing an entry (history log of a contact)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    date_edit = models.DateTimeField(_('last edit'), auto_now=True, blank=True, null=True)

    title = models.CharField(_('title'), max_length=20, blank=True, null=True)
    desc = models.CharField(_('description'), max_length=200, blank=True, null=True)


    def __str__(self):
        """ Class initialiser """
        return self.title.strip()


    def all(self):
        """ return a dict containing all attributes """
        return {
            attr: val
            for (attr, val) in vars(self).items()
            if not attr.startswith('_')
        }
