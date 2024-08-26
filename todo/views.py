from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.filter(is_completed = False)
    done_tasks = Task.objects.filter(is_completed = True)
    context = {
        'tasks':tasks,
        'done_tasks' : done_tasks
    }
    return render(request,'index.html',context)

def add_task(request):
    new_task = request.POST['task']
    Task.objects.create(task = new_task)
    return redirect('index')

def mark_as_done(request,pk):
    task = Task.objects.get(pk = pk)
    task.is_completed = True
    task.save()
    return redirect('index')

def undo_as_done(request,pk):
    done_task = Task.objects.get(pk = pk)
    done_task.is_completed = False
    done_task.save()
    return redirect('index')

def delete_task(request,pk):
    task = Task.objects.get(pk = pk)
    task.delete()
    return redirect('index')

def update(request,pk):
    task = Task.objects.get(pk = pk)
    context = {
        'task':task,
    }
    return render(request,'update.html',context)

def update_done(request,pk):
    edited_task = request.POST['edit_task']
    task = Task.objects.get(pk = pk)
    task.task = edited_task
    task.save()
    return redirect('index')