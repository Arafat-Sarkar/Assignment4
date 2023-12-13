from django import forms
from .models import Add_TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Add_TaskModel
        fields = '__all__'