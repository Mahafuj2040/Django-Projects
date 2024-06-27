from django.db import models
from category.models import TaskCategory

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.TextField()
    is_complete = models.BooleanField(default=False)
    
    task_assign_date = models.DateField()
    categories = models.ManyToManyField(TaskCategory)
    
    def __str__(self) -> str:
        return self.taskTitle