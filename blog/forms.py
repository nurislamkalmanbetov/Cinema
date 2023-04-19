from django import forms

from .models import *

from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(500)
        ]
    )



class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'duration', 'title', 'image', 'rental_start_date', 'rental_finish_date', 'sales_company', 'author', )


