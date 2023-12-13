from django.urls import path
from .import views

urlpatterns = [
    path('model/',views.addTaskModel, name= 'add_model' ),
    path('edit/<int:id>',views.edit_taks, name= "edit_task"),
    path('delet/<int:id>', views.delet_task,name= 'delet_task')
]
