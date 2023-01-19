from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Composition
from .forms import CompForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'compositions/index.html')
    
@login_required(login_url='login')
def compositions(request):
    compositions = Composition.objects.filter(status=1)
    return render(request, 'compositions/compositions.html', {'compositions':compositions})
    
@login_required(login_url='login')
def composition(request, prim_key):
    compositionObj = Composition.objects.get(id=prim_key)
    return render(request, 'compositions/single-composition.html', {'composition':compositionObj})

@login_required(login_url='login')
def createComposition(request):
    form = CompForm()

    if request.method == 'POST':
        form = CompForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('compositions')
    return render(request, 'compositions/comp-form.html', {'form':form})

@login_required(login_url='login')
def updateComposition(request, prim_key):
    composition = Composition.objects.get(id=prim_key)
    form = CompForm(instance=composition)

    if request.method =='POST':
        form = CompForm(request.POST, request.FILES,  instance=composition)
        if form.is_valid():
            form.save()
            return redirect('compositions')
    return render(request, 'compositions/comp-form.html', {'form':form})

@login_required(login_url='login')
def deleteComposition(request, prim_key):
    composition = Composition.objects.get(id=prim_key)
   
    if request.method =='POST':
        composition.delete()
        return redirect('compositions')
    return render(request, 'compositions/delete-obj.html', {'composition':composition})