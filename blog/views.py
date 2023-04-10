from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author
from django.db.models import Q


def home(request):
    return render(request, 'blog/welcome_page.html')


def about(request):
    return render(request, 'blog/about_page.html')


def blog_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_page.html', context)


def single_post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/single_post_page.html', context)


def posts_by_author(request, author_id):
    author = Author.objects.get(user=author_id)
    posts = Post.objects.filter(author=author_id)
    context = {
        'author': author,
        'posts': posts,
    }
    return render(request, 'blog/posts_by_author.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__contains=query) |
            Q(content__contains=query)
        ).distinct()
    context = {
        'queryset': queryset
    }
    return render(request, 'blog/search_page.html', context)


def add_post(request):
    return HttpResponse('New post page')
