from django.shortcuts import render
from .models import *
# Create your views here.

def HomePage(request):
    mainslider = MainSliderModel.objects.all()
    contex = {
        'mainslider':mainslider
    }
    return render (request, 'index.html',contex)
