from django.shortcuts import render,redirect
from app19.models import Country,State,City

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def add_country(request):
    return render(request,"add_country.html",{"data":Country.objects.all()})


def save_country(request):
    name = request.POST.get("t1")
    Country(country_name=name).save()
    return redirect('add_country')


def add_state(request):
    return render(request,"add_state.html",{"data":State.objects.all(),"c_data":Country.objects.all()})


def save_state(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    State(state_name=name,state_country_id=cno).save()
    return redirect('add_state')


def add_city(request):
    return render(request,"add_city.html",{"data":City.objects.all(),"s_data":State.objects.all()})


def save_city(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    City(city_name=name,city_state_id=cno).save()
    return redirect('add_city')