from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todo_app.models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')


def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def markAsUndone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task,
        }
        return render(request, 'editTask.html', context)


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')