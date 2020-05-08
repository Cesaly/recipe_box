from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
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


def staff_check(User):
    return User.is_staff


@login_required
def addrecipe(request):
    if request.method == 'POST':
        form = RecipeAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAddForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
@user_passes_test(staff_check)
def addauthor(request):
    if request.method == 'POST':
        form = AuthorAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAddForm()
    return render(request, 'generic_form.html', {'form': form})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'logout.html')


