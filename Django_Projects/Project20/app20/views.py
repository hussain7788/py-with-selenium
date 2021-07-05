from django.shortcuts import render,redirect
from app20.models import Employee

def showIndex(request):
    return render(request,"index.html",{"data":Employee.objects.all()})


def save_employee(request):
    name = request.POST.get("t1")
    salary = request.POST.get("t2")
    Employee(employee_name=name,employee_salary=salary).save()
    return redirect('main')