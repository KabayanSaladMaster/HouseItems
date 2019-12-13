from django.shortcuts import render
from .models import FrozenItem
from django.http import HttpResponse


# Create your views here.

def frozen(request):
    frozens = FrozenItem.objects.all().order_by('item_name')
    return render(request, 'frozen/frozen.html', {'frozens':frozens})

def frozen_details(request, slug):
    return HttpResponse(slug)