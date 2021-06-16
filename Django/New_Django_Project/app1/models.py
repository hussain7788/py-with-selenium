from django.db import models

# Create your models here.

class Products(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_photo = models.ImageField(upload_to="product_images/")


class Employee(models.Model):
    emp_name = models.CharField(max_length=40)
    emp_salary = models.FloatField()
    emp_degn = models.CharField(max_length=30)
    emp_photo = models.ImageField(upload_to="emp_images/")



