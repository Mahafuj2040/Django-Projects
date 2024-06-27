from django import forms
from django.forms.widgets import NumberInput
import datetime

class FormFeild(forms.Form):
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year2 = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    