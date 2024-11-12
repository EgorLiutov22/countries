from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

cities_info = {'paris': {'fact': 'Paris saint germain is 25-th team in champions ligue in current season ',
                         1924: '1924 Summer Olympics'
                         },
               'marselle': {'fact': 'fastest taxi'},
               1956: 'Honoré de Marseille'
               }


def index(request):
    template = loader.get_template("polls/index.html")
    context = dict()
    return HttpResponse(template.render(context, request))


def history(request):
    return HttpResponse('История')


def cities(request):
    if request.GET:
        city = request.GET.get('city')
        year = int(request.GET.get('year'))
        return HttpResponse(cities_info[city][year])
    else:
        return HttpResponse('Города')


def cities_about(request, city_name):
    return HttpResponse(cities_info[city_name]['fact'])


def facts(request):
    return HttpResponse('Факты')
