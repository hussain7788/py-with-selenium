import json
import re
from django.http import JsonResponse
from django.shortcuts import render
from .models import Student
# Create your views here.


def main(request):
    context = {"student": Student.objects.all()}
    return render(request, "ajax/main.html", context)


def add(request):
    if request.method == "POST":
        id = request.POST['id']
        na = request.POST['na']
        age = request.POST['age']
        if id == "":
            stu = Student(name=na, age=age)
        else:
            stu = Student(id=id, name=na, age=age)
        stu.save()
        data = Student.objects.values()
        data = list(data)
        return JsonResponse({"status": "saved", "data": data})


def delete(request):
    if request.method == "POST":
        id = request.POST['id']
        stu = Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({"status": "deleted"})


def update(request):
    if request.method == "POST":
        id = request.POST['id']
        data = Student.objects.get(id=id)
        data = {"id": data.id, "name": data.name, "age": data.age}
        return JsonResponse({"status": "up", "data": data})
