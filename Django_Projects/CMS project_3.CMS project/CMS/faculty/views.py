from django.shortcuts import render


def faculty_login(request):
    return render(request,"faculty/login.html")