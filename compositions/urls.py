from django.urls import path
from . import views

urlpatterns = [
    path('', views.compositions, name="home"),
    path('composition/<str:prim_key>/', views.composition, name="composition"),
    path('create-composition/', views.createComposition, name="create-composition"),
    path('update-composition/<str:prim_key>/', views.updateComposition, name="update-composition"),
    path('delete-composition/<str:prim_key>/', views.deleteComposition, name="delete-composition"),
]