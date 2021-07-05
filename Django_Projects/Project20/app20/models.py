from django.db import models

class Employee(models.Model):
    employee_idno = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=30)
    employee_salary = models.FloatField()

class Payment(models.Model):
    payment_no = models.AutoField(primary_key=True)
    payment_employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.DateField(default=None)