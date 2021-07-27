from django import forms
from django.db.models import fields
from .models import Core

class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = ['name']

    