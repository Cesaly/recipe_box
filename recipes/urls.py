from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index),
    path('recipe/<str:title>/', views.recipe),
    path('author/<str:name>/', views.author)
]