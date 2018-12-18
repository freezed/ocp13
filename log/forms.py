from django.forms import HiddenInput, ModelForm, ValidationError
from log.models import Entry


class EntryForm(ModelForm):

    class Meta:
        model = Entry
        fields = ['user', 'contact', 'title', 'desc']
        widgets = {
            'user': HiddenInput(),
            'contact': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Get back user & contact obj for `self.clean()`
        """
        user = kwargs.pop('user')
        contact = kwargs.pop('contact')
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = user
        self.fields['contact'].initial = contact


    def clean(self):
        """
        Checks if a entry is added on a contact owned by the connected user
        """
        cleaned_data = super(EntryForm, self).clean()

        if 'user' in self.changed_data or 'contact' in self.changed_data:
            raise ValidationError("Grrrrrr…!")

        if cleaned_data['contact'].user != cleaned_data['user']:
            raise ValidationError("Ce contact n'est pas un des vôtres")
