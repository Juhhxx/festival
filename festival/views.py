from django.shortcuts import render
from .models import *


def index_view(request):
    return render(request, 'festival/index.html')


def dias_view(request):
    dias = Dia.objects.all() 

    context = {'dias': dias}

    return render(request, 'festival/dias.html', context)



def concerto_view(request, id):
    concerto = Concerto.objects.get(id = id)

    context = {'concerto': concerto}

    return render(request, 'festival/concerto.html', context)

def palcos_view(request):
    palcos = Palco.objects.all()

    context = {'palcos': palcos}

    return render(request, 'festival/palcos.html', context)