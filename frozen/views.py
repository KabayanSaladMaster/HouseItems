from django.shortcuts import render
from .models import FrozenItem
from django.http import HttpResponse


# Create your views here.

def frozen(request):
    frozens = FrozenItem.objects.all()
    items = (
        FrozenItem.objects.all()[0],
    )
    return render(request, 'frozen/frozen.html', 
        {
         'Belly':frozens[0],
         'Chicharon':frozens[1],
         'RenoSpread':frozens[3],
         'ArgentinaSpread':frozens[2],
         'ArgentinaFSausage':frozens[5]
         },)

def frozen_details(request, slug):
    return HttpResponse(slug)