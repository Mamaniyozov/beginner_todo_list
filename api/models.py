from django.db import models


class Todolist(models.Model):
    task=models.CharField(max_length=500)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.id} {self.name}"

# Create your models here.
