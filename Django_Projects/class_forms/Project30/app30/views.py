from django.http import HttpResponse
from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")


def check(request):
    if request.method == "GET":
        return HttpResponse("Clicked on Get")
    else:
        return HttpResponse("Clicked on Post")
