from django.forms import ModelForm

from log.models import Entry


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'desc']
