from django.shortcuts import render
from ToDoList.settings import MEDIA_ROOT, MEDIA_URL
from ToDoListApp.models import AddTask

# Create your views here.

def homepage(request):
    context = {'success' : False}
    if request.method == 'POST':
        task_title = request.POST['task_title']
        task_desc = request.POST['task_desc']
        if len(request.FILES) !=0:
            task_img = request.FILES['task_img']

        insert_task = AddTask(TaskTitle=task_title, TaskDesc=task_desc, TaskImg = task_img)
        insert_task.save()
        context = {'success' : True}

    return render(request, 'homepage.html', context)

def tasks(request):
    allTasks = AddTask.objects.all()
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)


