from django.shortcuts import render
from .models import FrozenItem


# Create your views here.

def frozen(request):
    frozen = FrozenItem.objects.all()[0]
    return render(request, 'frozen/frozen.html', {'frozen':frozen})

def boost(request):
    return render(request, 'frozen/boost.html')