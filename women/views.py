from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main Page'
    }
    return render(request, 'women/index.html', context)

def show_post(request, post_id):
    return HttpResponse(f'show_post = {post_id}')


def about(request):
    context = {
        'menu': menu,
        'title': 'About'
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse('<h1>addpage</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')




def categories(request):
    return HttpResponse('<h1>women categories</h1>')