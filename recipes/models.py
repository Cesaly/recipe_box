from django.db import models

# Create your models here.
"""
Author
- name (CharField)
- bio (TextField)

Recipe
-Title (CharField)
-Author (ForeignKey)
-Description (TextField)
-Time required (CharField, ex: "One hour")
-Instructions (TextField)
"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(length=20)
    instructions = models.TextField()