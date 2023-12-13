from django.shortcuts import render
from TaskModel.models import Add_TaskModel
# from TaskCategory.models import AddCategory

def show_item(request):
    data = Add_TaskModel.objects.all()
    # data = AddCategory.objects.all()
    return render (request, 'show_task.html',{'data':data})