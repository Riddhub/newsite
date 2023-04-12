from django.urls import path

from women.views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/', categories),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

]
