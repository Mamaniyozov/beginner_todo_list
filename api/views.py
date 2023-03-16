from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpRequest
import json
from api.models import Todolist

def get_all_task(request:HttpRequest):
    if request.method=='GET':
        taskn=Todolist.objects.all
        result={
            "result":{}
        }
        for i in taskn:
            result.setdefault(i,[])
            result[i].append({          
                    'id':i.id,
                    "task":i.task,
                    'created_at':i.created_at,
                    'updated_at':i.updated_at
                    
                    
                    })
# Create your views here.
