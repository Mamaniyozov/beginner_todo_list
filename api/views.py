from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,HttpRequest
import json
from api.models import Todolist

def get_all_task(request:HttpRequest):
    if request.method=='GET':
        taskn=Todolist.objects.all()
        result={
            "result":{}
        }
        for i in taskn:
            name=i.task
            result.setdefault(i,[])
            result[i].append({          
                    'id':i.id,
                    "task":i.task,
                    'created_at':i.created_at,
                    'updated_at':i.updated_at
                    
                    
                    })
def delete_task(reqeust: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
    if reqeust.method == "POST":
        try:
            # get product from database by id
            product = Todolist.objects.get(id=pk)
            product.delete()
            return JsonResponse(product.to_dict())
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})
# Create your views here.
