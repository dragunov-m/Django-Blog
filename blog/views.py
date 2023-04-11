from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post, Author
from .forms import PostForm
from django.db.models import Q


def home(request):
    return render(request, 'blog/welcome_page.html')


def about(request):
    return render(request, 'blog/about_page.html')


def blog_page(request):
    posts = Post.objects.filter(featured=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_page.html', context)


def single_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user.is_authenticated:
        post.views += 1
        post.save()
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


@login_required()
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.author
            post.save()
            return redirect('blog:blog')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'blog/new_post_page.html', context)
