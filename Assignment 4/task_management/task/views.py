from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm
# Create your views here.


def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html', {'form' : task_form})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    
    if request.method =='POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
        
    return render(request, 'add_task.html', {'form' : task_form})



def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('homepage')


def complete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.is_complete =True
    task.save()
    return redirect('homepage')


def show_task(request):
    task = TaskModel.objects.all()
    for t in task:
        print(t)
        for i in t.categories.all():
            print(i)
            
    return render(request, 'show_tasks.html', {'tasks' : task})