from django.shortcuts import render,redirect
from .import forms
# from .forms import TaskModelForm
from .import models

# Create your views here.
def addTaskModel(request):
    if request.method == 'POST':
     form = forms.TaskModelForm(request.POST)
     if form.is_valid():
         form.save()
         return redirect('homepage')
     
     
    else:
        form = forms.TaskModelForm()
    return render(request, 'task_model.html',{'form':form  })


def edit_taks(request,id):
    edit = models.Add_TaskModel.objects.get(pk = id)
    form = forms.TaskModelForm(instance=edit)
    if request.method == 'POST':
     form = forms.TaskModelForm(request.POST, instance=edit)
     if form.is_valid():
         form.save()
         return redirect('homepage')
     
    
    
    return render(request, 'task_model.html',{'form':form  })
 
 
def delet_task(request,id):
    edit = models.Add_TaskModel.objects.get(pk = id)
    edit.delete()
    return redirect('homepage')
    