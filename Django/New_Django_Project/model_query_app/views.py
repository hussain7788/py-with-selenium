from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from New_Django_Project.settings import MOVIES_API_FILE
import json
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


def dict_data():
    dict_data = json.loads(open(MOVIES_API_FILE).read())
    titles = [x['title'][0:len(x['title']) - 1] for x in dict_data if
              x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                  'plot'] != '']
    posters = [x['poster'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    trailer_links = [x['trailer']['link'] for x in dict_data if
                     x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                         'plot'] != '']
    ratings = [x['rating'] for x in dict_data if
               x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                   'plot'] != '']
    plots = [x['plot'] for x in dict_data if
             x['title'] != '' and x['poster'] != '' and x['trailer']['link'] != '' and x['rating'] != '' and x[
                 'plot'] != '']

    # print(titles)
    # print(len(ratings))
    # print(len(posters))

    context = [{'title': title, 'poster': poster, 'rating': rating, 'plot': plot, 'trailer': trailer} for
               title, poster, rating, plot, trailer in zip(titles, posters, ratings, plots, trailer_links)]
    print("context::", context)
    return context


# Create your views here.
def movies_api_data(request):
    context = dict_data()
    return render(request, 'm_q_temp/movies_api.html', {'data': context})
