from django.shortcuts import render
from .models import FrozenItem
from django.http import HttpResponse


# Create your views here.

def frozen(request):
    frozens = FrozenItem.objects.all().order_by('item_name')
    items = (
        FrozenItem.objects.all()[0],
        FrozenItem.objects.all()[1],
        FrozenItem.objects.all()[2],
    )
    return render(request, 'frozen/frozen.html', 
        {
         'Belly':items[0],
         'Blood':items[1],
         'Liver':items[2],
         },)

def frozen_details(request, slug):
    return HttpResponse(slug)