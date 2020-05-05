from django.shortcuts import render, get_object_or_404
from recipes.models import Author, Recipe

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author_id=pk)
    return render(request, 'author.html', {'recipes': recipes, 'author': author})


def add_author(request):
    pass


def add_recipe(request):
    pass