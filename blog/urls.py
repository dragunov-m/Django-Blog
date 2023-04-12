from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/posts-by-<str:username>/', views.posts_by_author, name='posts_by_author'),
    path('blog/new-post/', views.add_post, name='new_post'),
    path('blog/post/<int:pk>/', views.single_post, name='post'),
    path('blog/search/', views.search, name='search'),
]
