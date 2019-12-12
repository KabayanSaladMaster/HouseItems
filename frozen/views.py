from django.shortcuts import render
from .models import FrozenItems

# Create your views here.

def frozen(request):
    frozen = FrozenItems.objects.all()[0]
    return render(request, 'frozen/frozen.html', {'frozen':frozen})

def boost(request):
    return render(request, 'frozen/boost.html')