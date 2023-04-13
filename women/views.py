from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def pageNotFound(request, exception):
    return HttpResponseNotFound('NOT FOUND')


def index(request):
    # posts = Women.objects.all()
    # cats = Category.objects.all()
    context = {
        # 'posts': posts,
        'menu': menu,
        # 'cats': cats,
        'title': 'Main Page',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context)



def show_category(request, cat_id):
    # posts = Women.objects.filter(cat_id=cat_id)
    # cats = Category.objects.all()

    # if len(posts) == 0:
    #     raise Http404()

    context = {
        # 'posts': posts,
        'menu': menu,
        # 'cats': cats,
        'title': 'Show Category',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context)


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