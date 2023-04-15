from django.urls import path

from women.views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('cats/', categories),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),

]
