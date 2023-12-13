from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def categories(request):
    if request.method =='POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
        
    else:
        
        form = forms.CategoryForm()
          
        return render(request, 'add_category.html', {'form': form })