from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description
        )
        return redirect('task_list')

    return render(request, 'tasks/create_task.html')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.is_completed = request.POST.get('is_completed') == 'on'
        task.save()

        return redirect('task_list')

    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')