from django import forms
from django.forms import ModelForm
from .models import Contacts, Job

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'position', 'date']

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'resume']