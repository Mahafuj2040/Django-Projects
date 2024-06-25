from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        add_form = forms.PostForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('add_post')
        
    else:
        add_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : add_form})



def edit_post(request, id):
    
    post = models.Post.objects.get(pk=id)
    add_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        add_form = forms.PostForm(request.POST, instance=post)
        if add_form.is_valid():
            add_form.save()
            return redirect('homepage')
        
    return render(request, 'add_post.html', {'form' : add_form})



def delete_post(request, id):
    
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')