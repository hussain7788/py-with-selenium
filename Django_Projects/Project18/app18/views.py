from django.shortcuts import render,redirect
from app18.models import CourseModel
from django.db.utils import IntegrityError

def showIndex(request):
    return render(request,"index.html")

def add_course(request):
    result = CourseModel.objects.all()
    return render(request,"add_course.html",{"data":result})

def save_course(request):
    name = request.POST.get("c1")
    fee = request.POST.get("c2")
    try:
        CourseModel(course_name=name,course_fee=fee).save()
        return redirect("add_course")
    except IntegrityError:
        result = CourseModel.objects.all()
        message = "Course Name is Taken"
        return render(request, "add_course.html", {"data": result,"error":message})


def add_student(request):
    course = CourseModel.objects.all()
    return render(request,"add_student.html",{"all_course":course})