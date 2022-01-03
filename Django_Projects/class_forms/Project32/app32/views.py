from django.shortcuts import render
from django.views.generic import TemplateView

# def showIndex(request):
#     return render(request,"index.html")


class OpenIndex(TemplateView):
    template_name = "index.html"