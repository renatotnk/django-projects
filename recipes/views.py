# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'recipes/home.html', status=200, context={
        'name': 'Test props'
    })
