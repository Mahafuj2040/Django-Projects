from django.shortcuts import render
from .forms import MusicianForm
from . import models
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class MusicianCreateView(CreateView):
    model = models.Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_editing'] = False
        return context


@method_decorator(login_required, name='dispatch')
class MusicianUpdateView(UpdateView):
    model = models.Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_editing'] = True
        return context
    

@method_decorator(login_required, name='dispatch')
class MusicianDeleteView(DeleteView):
    model = models.Musician
    template_name = 'musician_confirm_delete.html'
    success_url = reverse_lazy('homepage')




class MusicianListView(ListView):
    model = models.Musician
    template_name = 'home.html'
    context_object_name = 'musicians'
