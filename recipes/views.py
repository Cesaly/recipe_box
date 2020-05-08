from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from recipes.models import Author, Recipe
from recipes.forms import RecipeAddForm, AuthorAddForm, LoginForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def recipeview(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def authorview(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author_id=pk)
    return render(request, 'author.html', {'recipes': recipes, 'author': author})

@login_required
def addrecipe(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAddForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAddForm()
    return render(request, 'generic_form.html', {'form': form})


def loginview(request):
    if form.is_valid():
        form = LoginForm(request=POST)
        data = form.cleaned_data()
        user = authenticate(
            request, username=data['username'], password=data['password']
        )
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))

    form = LoginForm(request=POST)


def logoutview(request):
    pass