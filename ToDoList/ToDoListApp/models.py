from django.db import models

# Create your models here.
class AddTask(models.Model):
    TaskTitle = models.CharField(max_length=30)
    TaskDesc = models.TextField()
    TaskImg = models.ImageField(upload_to='uploads/', null=True, blank=True)
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TaskTitle