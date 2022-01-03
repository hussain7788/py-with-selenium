from django.shortcuts import render

def student_login(request):
    return render(request,"student/login.html")