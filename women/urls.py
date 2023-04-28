from django.urls import path

from women.views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('cats/', categories),
    path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact, name='contact'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('category/<slug:cat_slug>/', show_category, name='category'),

]
