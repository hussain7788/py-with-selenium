from django.db import models

# Create your models here.
from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    

    def __str__(self) -> str:
        return self.name
    
    