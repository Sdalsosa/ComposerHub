from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('newuser/', views.newUser, name="newuser"),
    path('', views.profiles, name="profiles"),
    path('users/', views.profiles, name="profiles"),
    path('profile/<str:prim_key>/', views.profile, name="profile"),
    path('account/', views.editProfile, name="account"),
    path('deluser/', views.delProfile, name="deluser"),
]