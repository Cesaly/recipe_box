from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from recipes.models import Author, Recipe
from recipes.forms import RecipeAddForm, AuthorAddForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def addrecipe(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAddForm()
    return render(request, 'generic_form.html', {'form': form})


def addauthor(request):

    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()
    return render(request, 'generic_form.html', {'form': form})


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author_id=pk)
    return render(request, 'author.html', {'recipes': recipes, 'author': author})