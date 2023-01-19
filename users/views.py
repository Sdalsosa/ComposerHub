from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()

    return render(request, 'users/profiles.html', {'profiles': profiles})

def profile(request, prim_key):
    profile= Profile.objects.get(id=prim_key)
    return render(request, 'users/user-profile.html', {'profile': profile})