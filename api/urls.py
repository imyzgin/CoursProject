from django.urls import path
from . import views

urlpatterns = [
    # path('tasks/', views.task_list, name='task_list'),
     path('', views.task_list, name ='index'),
     path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
     path('tasks/completed/', views.get_tasks_completed, name='get_tasks_completed'),
     path('tasks/uncompleted/', views.get_tasks_uncompleted, name='get_tasks_uncompleted'),
]