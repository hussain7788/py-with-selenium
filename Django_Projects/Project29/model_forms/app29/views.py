from django.shortcuts import redirect, render
from app29.forms import EmployeeForm
from django.contrib import messages


def showIndex(request):
    return render(request,"index.html",{"form":EmployeeForm()})


def save_employee(request):
    ef = EmployeeForm(request.POST,request.FILES)
    if ef.is_valid():
        ef.save()
        messages.success(request, "employee added successfully")
        return redirect("main")
    else:
        return render(request,"index.html",{"form":ef})
