from django import forms
from django.forms import ModelForm
from ToDoListApp.models import AddTask

class UpdateTask(ModelForm):
    class Meta:
        model = AddTask
        fields = '__all__'

        labels = {
            'TaskTitle' :  "Task Title",
            'TaskImg' :  "Images",
            'TaskDesc' : "Task Description",
        }

        widgets = {
            'TaskTitle' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Task Title'}),
            'TaskDesc' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Task Description'}),
        }