from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

# class MyEncoder(DjangoJSONEncoder):
#     def default(self, o):
#         if isinstance(o, Q):
#             ...

# {
#     "id": 1,
#     "title": "TestTask1",
#     "complition": false,
#     tags: [
#         {
#             "id" 1,
#             "name": asdasd
#         }
#     ]
# }

def task_list(request: HttpRequest):
    # if request.method == 'GET':
    #     tasks = Task.objects.all()
    #     tasks_data = serializers.serialize('json', tasks)  
    #     # print(tasks_data) 
    #     # for task in tasks:
    #     #     pass
    #     return JsonResponse(tasks.values().first(), safe=False)
   
    # if request.method == 'GET':
    #     tasks = Task.objects.values('id', 'title', 'complition', 'tag')
    #     tasks_list = list(tasks)
    #     return JsonResponse(tasks_list, safe=False)
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_list = []

        for task in tasks:
            tags = task.tag.all()
            tags_list = [{"id": tag.id, "name": tag.name} for tag in tags]
            task_dict = {
                "id": task.id,
                "title": task.title,
                "complition": task.complition,
                "tags": tags_list
            }
            tasks_list.append(task_dict)

        return JsonResponse(tasks_list, safe=False)


def task_detail(request: HttpRequest, task_id: int):
    if request.method == 'GET':
        # try:
            task = Task.objects.get(id=task_id)
            
            tags = task.tag.all()
            tags_list = [{"id": tag.id, "name": tag.name} for tag in tags]
            
            task_dict = {
                "id": task.id,
                "title": task.title,
                "complition": task.complition,
                "tags": tags_list
            }
            
            return JsonResponse(task_dict)
        # except Task.DoesNotExist:
        #     raise Http404("Task not found")


    
def get_tasks_completed(request: HttpRequest):
    # if request.method == 'GET':
    #     tasks = Task.objects.all()
    #     tasks_data = serializers.serialize('json', tasks)  
    #     # print(tasks_data) 
    #     # for task in tasks:
    #     #     pass
    #     return JsonResponse(tasks.values().first(), safe=False)
   
    # if request.method == 'GET':
    #     tasks = Task.objects.values('id', 'title', 'complition', 'tag')
    #     tasks_list = list(tasks)
    #     return JsonResponse(tasks_list, safe=False)
    if request.method == 'GET':
        tasks = Task.objects.filter(complition=True)
        tasks_list = []

        for task in tasks:
            tags = task.tag.all()
            tags_list = [{"id": tag.id, "name": tag.name} for tag in tags]
            task_dict = {
                "id": task.id,
                "title": task.title,
                "complition": task.complition,
                "tags": tags_list
            }
            tasks_list.append(task_dict)

        return JsonResponse(tasks_list, safe=False)


def get_tasks_uncompleted(request: HttpRequest):

    
    if request.method == 'GET':
        tasks = Task.objects.filter(complition=False)
        tasks_list = []

        for task in tasks:
            tags = task.tag.all()
            tags_list = [{"id": tag.id, "name": tag.name} for tag in tags]
            task_dict = {
                "id": task.id,
                "title": task.title,
                "complition": task.complition,
                "tags": tags_list
            }
            tasks_list.append(task_dict)

        return JsonResponse(tasks_list, safe=False)







    #   if request.method == 'GET':
    #     tasks = Task.objects.all()
    #     output = list()
    #     for task in tasks:
    #         # task_data = serializers.serialize('json', task)
    #         dict_task = dict()
    #         dict_task['title'] = task[0].title
    #         output.append(task_data)
    #     return JsonResponse(output, safe=False)
   

    # pass

