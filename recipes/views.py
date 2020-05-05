from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from recipes.models import Author, Recipe
from recipes.forms import RecipeAddForm

# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def addauthor(request):
    pass


def addrecipe(request):
    html = 'recipeaddform.html'
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        if form.is_valid():
            recipe = form.cleaned_data
            Recipe.objects.create(
                title=recipe['title'],
                author=recipe['author'],
                description=recipe['description'],
                time_required=recipe['time_required'],
                instructions=recipe['instructions']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAddForm()
    return render(request, html, {'form': form})


def recipe_view(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe.html', {'recipe': recipe})


def author_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    recipes = Recipe.objects.filter(author_id=pk)
    return render(request, 'author.html', {'recipes': recipes, 'author': author})