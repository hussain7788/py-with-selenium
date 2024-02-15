from django.db import models
from django.db.models import F, ExpressionWrapper, fields, Value
from django.db.models.functions import Now



class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, 
                                related_name='students')

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.FloatField()
    doj = models.DateField()
    dor = models.DateTimeField()
    city = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='employees')
    
    def __str__(self):
        return self.name
    
    @property
    def total_experience(self):
        today = Now()
        end_date = F('dor') if F('dor') is not None else today
        duration_days = ExpressionWrapper(end_date - F('doj'), output_field=fields.DurationField())
        total_years = ExpressionWrapper(duration_days / Value(365.25), output_field=fields.FloatField())
        return total_years
    


    
    