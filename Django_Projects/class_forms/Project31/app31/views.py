from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

def showIndex(request):
    return render(request,"index.html")

class CheckHttpMethod(View):
    def post(self,request):
        return HttpResponse("Click on Post")
    def get(self,request):
        return HttpResponse("Click on get")