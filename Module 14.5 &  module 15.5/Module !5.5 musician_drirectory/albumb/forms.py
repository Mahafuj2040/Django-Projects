from django import forms
from .models import Albumb


class AlbumbForm(forms.ModelForm):
    class Meta:
        model = Albumb
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }
        