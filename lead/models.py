import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    """
    Class implementing a contact
    Based on django.contrib.auth.models.AbstractUser
    Address, phone, URL & organization will move in dedicated table in future
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    date_edit = models.DateTimeField(_('last edit'), auto_now=True, blank=True, null=True)
    date_birthday = models.DateField(_('birth_date'), auto_now=False, auto_now_add=False, blank=True, null=True)
    address_label = models.CharField(_('address label'), max_length=50, blank=True)
    address_line_1 = models.CharField(_('address line 1'), max_length=50, blank=True)
    address_line_2 = models.CharField(_('address line 2'), max_length=50, blank=True)
    address_zip = models.CharField(_('zipcode'), max_length=50, blank=True)
    address_city = models.CharField(_('city'), max_length=50, blank=True)
    address_country = models.CharField(_('country'), max_length=50, blank=True)
    phone = models.CharField(_('phone'), max_length=50, blank=True)
    title = models.CharField(_('title'), max_length=50, blank=True)
    role = models.CharField(_('role'), max_length=50, blank=True)
    organization = models.CharField(_('organization'), max_length=50, blank=True)
    url = models.CharField(_('url') , max_length=50, blank=True)
    note = models.TextField(_('note'), blank=True)


    def __str__(self):
        """ Return shortname """
        return self.get_short_name()


    def all(self):
        """ return a dict containing all attributes """
        return {
            attr: val
            for (attr, val) in vars(self).items()
            if not attr.startswith('_')
        }


    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name


    def was_created_today(self):
        """ Return last contact created """
        return self.date_joined <= timezone.now() + datetime.timedelta(days=1)

    # TODO : this method schould avoid setting`success_url` in `lead.views`
    # TODO : see https://docs.djangoproject.com/fr/2.1/ref/models/instances/#django.db.models.Model.get_absolute_url
    # TODO : see https://docs.djangoproject.com/fr/2.1/topics/class-based-views/generic-editing/#model-forms
    # def get_absolute_url(self):
        # return reverse('contact:view', kwargs={'contact_id': self.contact_id})
