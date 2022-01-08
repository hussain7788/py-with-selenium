from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.


def index(request):
    company = Company.objects.all()[:3]
    language = Language.objects.all()

    lan = language.filter(name="php").get()
    print("lan::", lan.programmer_set.all())
    programme = Programmer.objects.all()
    pro = Programmer.objects.filter(name__contains="mu")
    for i in pro:
        print("object::", i.name, i.age, i.company, i.language)
        for lang in i.language.all():
            print("language::", lang)
    print(pro)

    # OR operator to query model
    # programme = programme.filter(Q(age__gte=20) | Q(age__lte=24))
    # AND operator to query model
    programme = programme.filter(Q(age__gte=20) & Q(age__lte=24))

    print(programme)

    return render(request, "m_q_temp/index.html", {"company": company, "language": language, "programmer": programme})
