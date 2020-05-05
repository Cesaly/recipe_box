from django.contrib import admin
from django.urls import path
from django.shortcuts import reverse
from recipes import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<int:pk>/', views.recipe_view, name='recipe_view'),
    path('author/<int:pk>/', views.author_view, name='author_view'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('addrecipe/', views.addrecipe, name='addrecipe')
]