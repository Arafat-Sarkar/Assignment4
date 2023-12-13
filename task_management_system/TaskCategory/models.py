from django.db import models
# from TaskModel.models import Add_TaskModel

# Create your models here.
class AddCategory(models.Model):
    categoryName = models.CharField(max_length=200)
    # tasks = models.ManyToManyField(Add_TaskModel)
   
   
    def __str__(self):
        return self.categoryName
    