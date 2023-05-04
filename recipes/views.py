from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'recipes/home.html')


def about(req):
    return HttpResponse('ABOUT')


def contact(req):
    return HttpResponse('CONTACT')
