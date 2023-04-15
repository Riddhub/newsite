from django import template
from women.models import *


register = template.Library()


# @register.simple_tag(name='getcats')
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)
#
#
# @register.simple_tag()
# def get_posts(filter=None):
#     if not filter:
#         return Women.objects.all()
#     else:
#         return Women.objects.filter(cat=filter)


@register.inclusion_tag(filename='women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag(filename='women/list_posts.html')
def show_posts(filter=None):
    if not filter:
        posts = Women.objects.all()
        # posts = Women.objects.filter(cat__slug=filter)
    else:
        posts = Women.objects.filter(cat__slug=filter)

    return {'posts': posts}


