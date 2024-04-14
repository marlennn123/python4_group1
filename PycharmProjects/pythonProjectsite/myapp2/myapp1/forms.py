from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'marca', 'model', 'description', 'price', 'year', 'box',]