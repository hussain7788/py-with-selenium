from django.shortcuts import render


def showLogin(request):
    return render(request,"hod/login.html")