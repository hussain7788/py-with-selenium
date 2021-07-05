from django.shortcuts import render
from app27.forms import *

def showIndex(request):
    return render(request,"index.html",{"form":RegistrationForm()})


def register_employee(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    contact = request.POST.get("cno")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    desg = request.POST.get("designation")
    join = request.POST.get("doj")
    birth = request.POST.get("dob")

    print(idno)
    print(name)
    print(contact)
    print(gender)
    print(email)
    print(desg)
    print(join)
    print(birth)

    return render(request, "success.html")