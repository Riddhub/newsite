from django.http import HttpResponse
from django.shortcuts import render

from .models import *
menu = ['about', 'add', 'login']

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main Page'
    }

    return render(request, 'women/index.html', context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About'})


def categories(request):
    return HttpResponse('<h1>women categories</h1>')