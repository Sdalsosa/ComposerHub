from django.urls import path
from . import views

urlpatterns = [
    path('', views.compositions, name="compositions"),
    path('composition/<str:prim_key>/', views.composition, name="composition"),
    path('create-composition/', views.createComposition, name="create-composition"),
]