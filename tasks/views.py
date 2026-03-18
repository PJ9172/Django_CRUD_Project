from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .forms import TaskForm

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'tasks/create_task.html', {'form': form})

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()
        return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')

    return render(request, 'tasks/delete_task.html', {'task': task})