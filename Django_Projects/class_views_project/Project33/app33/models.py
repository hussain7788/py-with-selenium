from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    photo = models.ImageField(upload_to="employee_images/")


class UserModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    password = models.CharField(max_length=30)

