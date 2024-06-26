from django.shortcuts import render, redirect
from .forms import MusicianForm
from . import models

def add_musician(request):
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = MusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form})

def musician_edit(request, id):
    musician = models.Musician.objects.get(pk=id)
    if request.method == 'POST':
        musician_form = MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'form': musician_form})

def musician_delete(request, id):
    musician = models.Musician.objects.get(pk=id)
    musician.delete()
    return redirect('homepage')

def musician_list(request):
    musicians = models.Musician.objects.all()
    return render(request, 'home.html', {'musicians': musicians})
