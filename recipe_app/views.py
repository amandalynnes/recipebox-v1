from django.shortcuts import render

from recipe_app.models import Author, RecipeItem

# Create your views here.


def index_view(request):
    recipes = RecipeItem.objects.all()
    return render(request, "index.html", {
        "heading": "Recipebox!", "recipes": recipes
    })


def recipe_detail(request, recipe_id):
    recipe = RecipeItem.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"recipe": recipe})


def author_detail(request, author_id):
    author_obj = Author.objects.get(id=author_id)
    recipes = RecipeItem.objects.filter(author=author_obj)

    return render(request, "author_detail.html", {
        "author": author_obj,
        "recipes": recipes
    })
