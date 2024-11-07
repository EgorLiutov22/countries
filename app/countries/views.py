from django.http import HttpResponse

cities_info = {'paris': {'fact': 'Paris saint germain is 25-th team in champions ligue in current season ',
                         1924: '1924 Summer Olympics'
                         },
               'marselle': {'fact': 'fastest taxi'},
               1956: 'Honoré de Marseille'
               }


def index(request):
    res = '''<a href=/history>История</a><br>
    <a href=/cities>Города</a>'''
    return HttpResponse(res)


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
