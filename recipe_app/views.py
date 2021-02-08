from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_app.models import Author, RecipeItem
from recipe_app.forms import AddRecipeForm, AddAuthorForm

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


def add_recipe(request):
    context = {}

    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_item = RecipeItem.objects.create(
               title=data['title'],
               author=data['author'],
               description=data['description'],
               time_required=data['time_required'],
               instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('recipe_detail', args=[new_item.id]))

    form = AddRecipeForm()
    context.update({'form': form})
    return render(
        request,
        # "GenericForm.html",
        "add_recipe.html",
        context
    )


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()
    return render(request, 'add_author.html', {'form': form})
