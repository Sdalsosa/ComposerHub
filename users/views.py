from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from .forms import NewUserForm, AccountForm
from django.db.models import Q

# Create your views here.


def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Invalid Username")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("compositions")
        else:
            messages.error(request, "Incorrect Username or Password")

    return render(request, "users/signin_up.html")


@login_required(login_url="login")
def userLogout(request):
    logout(request)
    messages.success(request, "Come back soon!")
    return redirect("home")


def newUser(request):
    page = "newuser"
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "Registration Successful!")

            login(request, user)
            return redirect("account")

        else:
            messages.error(request,
                           "Registration Failed! Make sure passwords match")

    return render(request, "users/signin_up.html",
                  {"page": page, "form": form})


def profiles(request):
    search_composer = ""

    if request.GET.get("search_composer"):
        search_composer = request.GET.get("search_composer")

    profiles = Profile.objects.filter(
        Q(first_name__icontains=search_composer) |
        Q(last_name__icontains=search_composer)
    )

    return render(
        request,
        "users/profiles.html",
        {"profiles": profiles, "search_composer": search_composer},
    )


def profile(request, prim_key):
    profile = Profile.objects.get(id=prim_key)
    return render(request, "users/user-profile.html", {"profile": profile})


@login_required(login_url="login")
def editProfile(request):
    currentUser = request.user.profile
    form = AccountForm(instance=currentUser)
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=currentUser)
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Successful")
            return redirect("compositions")

    return render(request, "users/account.html", {"form": form})


@login_required(login_url="login")
def delProfile(request):
    currentUser = request.user.profile
    currentUser.delete()
    messages.success(request, "The user is deleted")
    return redirect("home")
