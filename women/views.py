from django.contrib import auth
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]


def pageNotFound(request, exception):
    return HttpResponseNotFound('NOT FOUND')


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    # context_object_name = 'posts'
    # extra_context = {'title': 'Main Page'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main Page'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     context = {
#         'menu': menu,
#         'title': 'Main Page',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context)


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#         # 'cat_selected': post.cat__slug,
#     }
#     return render(request, 'women/post.html', context)


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


def show_category(request, cat_slug):
    # cat = get_object_or_404(Women, slug=cat_slug)
    context = {
        # 'cat': cat,
        'menu': menu,
        'title': 'Show Category',
        'cat_selected': cat_slug,
    }
    return render(request, 'women/index.html', context)


# class WomenCategory(ListView):
#     model = Women
#     template_name = 'women/index.html'
#     context_object_name = 'posts'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Categoty -' + str(context['posts'][0].cat)
#         context['cat_selected'] = context['posts'][0].cat_id
#         return context


def about(request):
    context = {
        'menu': menu,
        'title': 'About',
    }
    return render(request, 'women/about.html', context=context)


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     context = {
#         'menu': menu,
#         'title': 'AddPage',
#         'form': form,
#
#     }
#     return render(request, 'women/addpage.html', context=context)


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Add Page'
        return context


def contact(request):
    return HttpResponse('<h1>contact</h1>')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {
        'menu': menu,
        'title': 'Login',
        'form': form,
    }
    return render(request, 'women/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()
    context = {
        'menu': menu,
        'title': 'Register',
        'form': form,
    }
    return render(request, 'women/register.html', context)


def categories(request):
    return HttpResponse('<h1>women categories</h1>')