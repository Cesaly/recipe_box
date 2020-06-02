from django.contrib import admin
from django.urls import path
from django.shortcuts import reverse
from recipes import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:pk>/', views.recipeview, name='recipeview'),
    path('author/<int:pk>/', views.authorview, name='authorview'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview')
]