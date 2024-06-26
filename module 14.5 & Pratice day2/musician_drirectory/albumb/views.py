from django.shortcuts import render, redirect
from .forms import AlbumbForm
from . import models

# Create your views here.

def add_albumb(request):
    if request.method == 'POST':
        album_form = AlbumbForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_albumb')
        
    else:
        album_form = AlbumbForm()
    return render(request, 'add_albumb.html', {'form' : album_form})

def edit_albumb(request, id):
    albumn = models.Albumb.objects.get(pk=id)
    if request.method == 'POST':
        albumb_form = AlbumbForm(request.POST, instance=albumn)
        if albumb_form.is_valid():
            albumb_form.save()
            return redirect('homepage')
    else:
        albumb_form = AlbumbForm(instance=albumn)
    return render(request, 'add_albumb.html', {'form': albumb_form})

def delete_albumb(request, id):
    albumn = models.Albumb.objects.get(pk=id)
    albumn.delete()
    return redirect('homepage')



