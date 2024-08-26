from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add_task,name='add_task'),
    path('mark/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('undo/<int:pk>/',views.undo_as_done,name='undo_as_done'),
    path('delete/<int:pk>/',views.delete_task, name='delete_task'),
    path('update/<int:pk>/',views.update, name='update_task'),
    path('edit/<int:pk>/',views.update_done, name="update_done")

]