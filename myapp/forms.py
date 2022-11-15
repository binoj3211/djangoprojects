from django import forms
from django.contrib.auth.forms import UserCreationForm

# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()
    email_address = forms.EmailField(max_length = 150)
