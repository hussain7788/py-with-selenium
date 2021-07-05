from django.shortcuts import render,redirect
from app29.forms import EmployeeForm

def showIndex(request):
    return render(request,"index.html",{"form":EmployeeForm()})


def save_employee(request):
    ef = EmployeeForm(request.POST,request.FILES)
    if ef.is_valid():
        ef.save()
        return redirect('main')
    else:
        return render(request,"index.html",{"form":ef})