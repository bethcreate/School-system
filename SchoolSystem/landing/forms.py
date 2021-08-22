from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Landing

class LandingRegistrationForm(forms.ModelForm):
    class Meta:
        model= Landing
        fields = "__all__"