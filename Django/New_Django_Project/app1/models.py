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

class Person(models.Model):
    p_name = models.CharField(max_length=50)
    p_age = models.IntegerField()
    p_num = models.IntegerField(unique=True)
    p_gender = models.CharField(max_length=10, null=True)

class Company(models.Model):
    c_name = models.CharField(max_length=50)

    def __str__(self):
        return self.c_name

class Language(models.Model):
    l_name = models.CharField(max_length=30)

    def __str__(self):
        return self.l_name

class Programmer(models.Model):
    p_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    p_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    p_language = models.ManyToManyField(Language)

    def __str__(self):
        return self.p_name






