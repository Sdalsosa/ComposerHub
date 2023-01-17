from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('users/', views.profiles, name="profiles"),
]