from django.urls import path
from ToDoListApp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tasks/', views.tasks, name='tasks'),
    path('update/<task_id>', views.update_task, name='update_task_link'),
    path('delete/<task_id>', views.delete_task, name='delete_task_link'),
]