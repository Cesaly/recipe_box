from django import forms
from recipes.models import Author, Recipe


class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'author',
            'description',
            'time_required',
            'instructions'
        ]


class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name'
        ]


