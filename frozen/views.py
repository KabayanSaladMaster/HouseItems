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
         'Chicharon':frozens[1],
         'ArgentinaSpread':frozens[2],
         'RenoSpread':frozens[3],
         'ArgentinaSSisig':frozens[4],
         'ArgentinaFSausage':frozens[5],

         'Belly':frozens[0],
         'PorkChop':frozens[6],
         'TenderJumbo':frozens[7],
         'TenderClassic':frozens[8],
         'Longanisa':frozens[9],
         'Tocino':frozens[10],
         'PorkBlood':frozens[11],
         'EarChop':frozens[12],
         'Throaters':frozens[13],
         'RibsChop':frozens[14],
         'PataSlice':frozens[15],
         },)

def frozen_details(request, slug):
    return HttpResponse(slug)