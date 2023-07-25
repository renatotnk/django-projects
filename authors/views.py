from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RegisterForm


# Create your views here.
def register_view(req):
    register_form_data = req.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)
    return render(req, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(req):
    if not req.POST:
        raise Http404()

    POST = req.POST
    req.session['register_form_data'] = POST
    form = RegisterForm(POST) # noqa f841

    if form.is_valid():
        form.save()
        messages.success(req, 'Your user was created! Please log in.')

        del (req.session['register_form_data'])

    return redirect('authors:register')
