from django import forms

from .models import *


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('name', 'duration', 'title', 'image', 'rental_start_date', 'rental_finish_date', 'sales_company', 'author', )
        