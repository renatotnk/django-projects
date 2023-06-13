from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# from utils.recipes.factory import make_recipe


# Create your views here.


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(req, 'recipes/pages/home.html', status=200, context={
        'recipes': recipes,
    })


def category(req, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(req, 'recipes/pages/category.html', status=200, context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}  - Category | '
    })


def recipe(req, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(req, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(req):
    ...
