from django import forms
from .models import Albumb


class AlbumbForm(forms.ModelForm):
    class Meta:
        model = Albumb
        fields = '__all__'