from django.shortcuts import render, HttpResponseRedirect, reverse

from recipe_app.models import Author, RecipeItem
from recipe_app.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# Create your views here.


def index_view(request):
    recipes = RecipeItem.objects.all()
    return render(request, "index.html", {
        "heading": "Recipebox!", "recipes": recipes
    })


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse("homepage"))

    form = LoginForm()
    return render(request, "generic_form.html", {'form': form})


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
               author=request.user.author,
               description=data['description'],
               time_required=data['time_required'],
               instructions=data['instructions']
            )
            return HttpResponseRedirect(reverse('recipe_detail', args=[new_item.id]))

    form = AddRecipeForm()
    context.update({'form': form})
    return render(
        request,
        # "generic_form.html",
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
