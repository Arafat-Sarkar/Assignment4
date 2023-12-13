from django.db import models
from TaskCategory.models import AddCategory

# Create your models here.
class Add_TaskModel(models.Model):
     taskTitle = models.CharField(max_length=200)
     taskDescription = models.TextField()
     is_completed = models.BooleanField(default=False)
     taskAssignDate = models.DateField()
     taks = models.ManyToManyField(AddCategory)
     
     def __str__(self):
        return self.taskTitle
    