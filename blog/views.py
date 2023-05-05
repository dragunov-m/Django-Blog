from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import Http404
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from django.views.generic.edit import FormMixin
from .models import Post
from .forms import PostForm
from blog_comments.forms import CommentForm
User = get_user_model()

# TODO: Fix profile images in posts and comments (issue is in logic)


class HomePage(TemplateView):
    template_name = 'blog/welcome_page.html'

# def home(request):
#     return render(request, 'blog/welcome_page.html')


class AboutPage(TemplateView):
    template_name = 'blog/about_page.html'

# def about(request):
#     return render(request, 'blog/about_page.html')


class BlogPage(ListView):
    model = Post
    template_name = 'blog/blog_page.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(featured=True).order_by('-timestamp')
        return queryset


# class BlogPageAPI(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = BlogPageSerializer

# def blog_page(request):
#     posts = Post.objects.filter(featured=True)
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/blog_page.html', context)


class PostPage(FormMixin, DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if self.request.user.is_authenticated:
            obj.views += 1
            obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comment_set.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.path


# def single_post(request, pk):
#     post = Post.objects.get(id=pk)
#     if request.user.is_authenticated:
#         post.views += 1
#         post.save()
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/single_post_page.html', context)


class AuthorPost(ListView):
    model = Post
    template_name = 'blog/posts_by_author.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        author = User.objects.get(username=self.kwargs['username'])
        queryset = super().get_queryset().filter(author__user_id=author)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.get(username=self.kwargs['username'])
        return context

# def posts_by_author(request, username):
#     author = User.objects.get(username=username)
#     posts = Post.objects.filter(author__user_id=author)
#     context = {
#         'author': author,
#         'posts': posts,
#     }
#     return render(request, 'blog/posts_by_author.html', context)


class SearchPost(ListView):
    model = Post
    template_name = 'blog/search_page.html'
    context_object_name = 'queryset'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__contains=query) |
                Q(content__contains=query)
            ).distinct()
        return queryset

# def search(request):
#     queryset = Post.objects.all()
#     query = request.GET.get('q')
#     if query:
#         queryset = queryset.filter(
#             Q(title__contains=query) |
#             Q(content__contains=query)
#         ).distinct()
#     context = {
#         'queryset': queryset
#     }
#     return render(request, 'blog/search_page.html', context)


class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/new_post_page.html'
    success_url = reverse_lazy('blog:blog')
    login_url = 'blog_auth:login'

    def form_valid(self, form):
        form.instance.author = self.request.user.author
        return super().form_valid(form)

# CBV AddPost with get and post methods


# class AddPost(LoginRequiredMixin, CreateView):
#     form_class = PostForm
#     template_name = 'blog/new_post_page.html'
#     login_url = 'blog_auth:login'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class
#         context = {
#             'form': form,
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user.author
#             post.save()
#             return redirect('blog:blog')
#         context = {
#             'form': form
#         }
#         return render(request, self.template_name, context)


# FBV AddPost


# @login_required(login_url='blog_auth:login')
# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user.author
#             post.save()
#             return redirect('blog:blog')
#     else:
#         form = PostForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'blog/new_post_page.html', context)

class EditPost(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edit_post.html'
    success_message = 'Your post is updated'
    login_url = 'blog_auth:login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user.author:
            raise Http404("You are not allowed to edit this Post")
        return super(EditPost, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path
