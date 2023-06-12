from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from todo_app.models import Task


def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')