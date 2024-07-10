from django.shortcuts import render
from . forms import FormFeild
# Create your views here.

def pratice_form(requet):
    form = FormFeild()
    return render(requet, 'index.html', {'form' : form})