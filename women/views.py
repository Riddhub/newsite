from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('women app page')


def categories(request):
    return HttpResponse('<h1>women categories</h1>')