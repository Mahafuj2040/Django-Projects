from django.shortcuts import render, redirect
from .forms import AlbumbForm
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Albumb
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.



@method_decorator(login_required, name='dispatch')
class AlbumbCreate(CreateView):
    model = Albumb
    form_class = AlbumbForm
    template_name = 'add_albumb.html'
    success_url = reverse_lazy('add_albumb')
    
    
@method_decorator(login_required, name='dispatch')  
class AlbumbUpdate(UpdateView):
    model = Albumb
    form_class = AlbumbForm
    template_name = 'add_albumb.html'
    success_url = reverse_lazy('add_albumb')

@login_required
def delete_albumb(request, id):
    albumn = Albumb.objects.get(pk=id)
    albumn.delete()
    return redirect('homepage')