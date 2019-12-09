from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    subject = forms.CharField(max_length = 100)
