# Core Django
from django.urls import path

# blog app
from .views import AddPost, HomePage, AboutPage, BlogPage, PostPage, AuthorPost, SearchPost, EditPost

app_name = 'blog'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('blog/<str:username>/posts/', AuthorPost.as_view(), name='posts_by_author'),
    path('blog/new-post/', AddPost.as_view(), name='new_post'),
    path('blog/edit-post/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('blog/post/<int:pk>/', PostPage.as_view(), name='post'),
    path('blog/search/', SearchPost.as_view(), name='search'),
]
