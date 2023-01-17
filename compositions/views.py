from django.shortcuts import render
from django.views import generic, View
from .models import Composition

# Create your views here.

def compositions(request):
    compositions = Composition.objects.all()
    return render(request, 'compositions/compositions.html', {'compositions':compositions})

def composition(request, prim_key):
    compositionObj = Composition.objects.get(id=prim_key)
    return render(request, 'compositions/single-composition.html', {'composition':compositionObj})