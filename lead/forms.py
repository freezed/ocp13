from django.forms import ModelForm

from lead.models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = ['user','date_joined']
        localized_fields = '__all__'
