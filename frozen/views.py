from django.shortcuts import render

# Create your views here.

def frozen(request):
    return render(request, 'frozen/frozen.html')
