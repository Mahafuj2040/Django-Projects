from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def add_profile(request):
    if request.method == 'POST':
        profile_forms = forms.ProfileForm(request.POST)
        if profile_forms.is_valid():
            profile_forms.save()
            return redirect('add_profile')
        
    else:
        profile_forms = forms.ProfileForm()
    # return render(request, 'add_profile.html', {'form' : profile_forms})
    return render(request, 'add_profile.html', {'form' : profile_forms})