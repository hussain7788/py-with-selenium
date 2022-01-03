from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.FloatField()
    designation = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='employee_photo/')
    langs = models.CharField(max_length=100)