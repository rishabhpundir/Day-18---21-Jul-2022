from django.shortcuts import render, HttpResponseRedirect
from ToDoListApp.models import AddTask
from templates.forms import UpdateTask

# Create your views here.

def homepage(request):
    if request.method == "POST":
        form = UpdateTask(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks')
    else:
        form = UpdateTask
    
    return render(request, 'homepage.html', {'form':form,})

def tasks(request):
    allTasks = AddTask.objects.all()
    return render(request, 'tasks.html', {'tasks' : allTasks,})

def update_task(request, task_id):
    task= AddTask.objects.get(pk=task_id)
    form = UpdateTask(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(f'/tasks?updated=True')
    return render(request, 'update_task.html', {'form': form,})

def delete_task(request, task_id):
    task_del = AddTask.objects.get(pk=task_id)
    task_del.delete()
    print(task_del)
    return HttpResponseRedirect('/tasks')


