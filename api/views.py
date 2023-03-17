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
            
            result.setdefault(i,[])
            result[i].append({          
                    'id':id,
                    "task":i.task,
                    "task_text":i.task_text,
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
def get_update_task(request: HttpRequest, pk: int):
     if request.method=='GET':
        # Get the smartphone object
        tas = Todolist.objects.get(id=pk)
        # Get the price from the request
        price = tas.id
        # Update the price
        tas.task= price
        tas.save
        return JsonResponse({
            "task":tas.task,
            "created_at":tas.created_at,
            "updated_at":tas.updated_at
        })
def add_task(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    if reqeust.method == 'POST':
        # get body from request
        body = reqeust.body
        # get body data
        decoded = body.decode()
        # data to dict
        data = json.loads(decoded)
        task= data.get("task",False)
        task_text=data.get("task_text",False)
        if task == False:
            return JsonResponse({"status": "price field is required."})
        if task_text == False:
            return JsonResponse({"status": "price field is required."})
        fix=Todolist()
        fix.task=task
        fix.task_text=task_text
        fix.save



        return JsonResponse({'result':data})
    
    return JsonResponse({})
# Create your views here.
