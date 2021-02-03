from django.db import models

# Create your models here.
"""
Author model:
---
Name (CharField)
Bio (TextField)

Recipe Model:
---
Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""


class Author(models.Model):
    name = models.CharField(max_length=150)
    bio = models.TextField()


class RecipeItem(models.Model):
    title = models.CharField(max_length=40)
    author = ''
    description = models.TextField()
    time_required = models.CharField(max_length=100)
    instructions = models.TextField()