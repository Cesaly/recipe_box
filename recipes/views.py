from django.shortcuts import render

from recipes.models import Author, Recipe

# Create your views here.
def index(request):
    data = Recipe.objects.all()
    return render(request, 'index.html', {'data': data})

def recipe(request, title):
    data = Recipe.objects.get(title=title)
    return render(request, 'recipe.html', {'data': data})

def author(request, name):
    author = Author.objects.get(name=name)
    data = Recipe.objects.get(author=author)
    return render(request, 'author.html', {'data': data})