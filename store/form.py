from django.forms import ModelForm, TextInput, EmailInput,Textarea
from.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': 'Nom',
            'email': 'E-mail',
            'message': 'Message'
        }
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
            'message':Textarea(attrs={'class':'form-control'})
        }


class BookingForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        exclude = ['message']
        labels = {
            'name': 'Nom',
            'email': 'E-mail',
        }
        widgets = {
            'name': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'})
        }

