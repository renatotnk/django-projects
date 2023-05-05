# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'recipes/pages/home.html', status=200, context={
        'name': 'Test props'
    })


def recipe(req, id):
    return render(req, 'recipes/pages/recipe-view.html', status=200, context={
        'name': 'Test props'
    })
