from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Composition
from .forms import CompForm

# Create your views here.

def compositions(request):
    compositions = Composition.objects.all()
    return render(request, 'compositions/compositions.html', {'compositions':compositions})

def composition(request, prim_key):
    compositionObj = Composition.objects.get(id=prim_key)
    return render(request, 'compositions/single-composition.html', {'composition':compositionObj})

def createComposition(request):
    form = CompForm()

    if request.method == 'POST':
        form = CompForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'compositions/comp-form.html', {'form':form})


def updateComposition(request, prim_key):
    composition = Composition.objects.get(id=prim_key)
    form = CompForm(instance=composition)

    if request.method =='POST':
        form = CompForm(request.POST, request.FILES,  instance=composition)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'compositions/comp-form.html', {'form':form})


def deleteComposition(request, prim_key):
    composition = Composition.objects.get(id=prim_key)
   
    if request.method =='POST':
        composition.delete()
        return redirect('home')
    return render(request, 'compositions/delete-obj.html', {'composition':composition})