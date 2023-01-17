from django.shortcuts import render

# Create your views here.

def compositions(request):
    return render(request, 'compositions/compositions.html')

def composition(request, prim_key):
    return render(request, 'compositions/single-composition.html')