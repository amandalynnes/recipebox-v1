from django.shortcuts import render

from recipe_app.models import Author, RecipeItem

# Create your views here.


def index_view(request):
    recipes = RecipeItem.objects.all()
    return render(request, "index.html", {
        "heading": "Recipes!", "recipes": recipes
    })


def recipe_detail(request, recipe_id):
    recipe = RecipeItem.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})
