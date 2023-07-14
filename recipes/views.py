import os

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes.models import Recipe
from utils.pagination import make_pagination

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

# Create your views here.


def home(req):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    # messages.success(req, 'Epa, você foi pesquisar algo que eu vi.')

    page_obj, pagination_range = make_pagination(req, recipes, PER_PAGE)

    return render(req, 'recipes/pages/home.html', status=200, context={
        'recipes': page_obj,
        'pagination_range': pagination_range
    })


def category(req, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(req, recipes, PER_PAGE)

    return render(req, 'recipes/pages/category.html', status=200, context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name}  - Category | '
    })


def recipe(req, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(req, 'recipes/pages/recipe-view.html', status=200, context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(req):
    search_term = req.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        # __icontains === SELECT recipe WHERE title LIKE search_term
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(req, recipes, PER_PAGE)

    return render(req, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })
