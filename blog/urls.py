from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/new-post/', views.add_post, name='new_post'),
    path('blog/<int:pk>/', views.single_post, name='post'),
]
