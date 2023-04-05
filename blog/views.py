from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    return HttpResponse('Hello page')


def blog_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_page.html', context)


def add_post(request):
    return HttpResponse('New post page')


def single_post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/single_post_page.html', context)
