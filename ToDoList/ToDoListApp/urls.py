from django.urls import path
from ToDoListApp import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('tasks/', views.tasks, name='tasks')
]