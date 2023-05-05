# from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe

# Create your views here.


def home(req):
    return render(req, 'recipes/pages/home.html', status=200, context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(req, id):
    return render(req, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
