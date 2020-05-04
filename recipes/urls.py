from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index),
    path('recipe/<int:pk>/', views.recipe_view, name='recipe_view'),
    path('author/<int:pk>/', views.author_view, name='author_view')
]