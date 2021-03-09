from django.db import models
from django.contrib.auth.models import User


# Create your models here.
"""
User:
---
username
password
email

one to one

Author model:
---
Name (CharField)
Bio (TextField)

one to many

Recipe Model:
---
Title (CharField)
Author (ForeignKey)
Description (TextField)
Time Required (Charfield) (for example, "One hour")
Instructions (TextField)
"""


class Author(models.Model):
    author = models.CharField(max_length=150)
    bio = models.TextField()
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    favorites = models.ManyToManyField('RecipeItem', related_name='favorite', symmetrical=False)

    def __str__(self):
        return self.author


class RecipeItem(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.author}"
