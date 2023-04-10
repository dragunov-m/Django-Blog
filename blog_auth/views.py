from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


@login_required
def profile(request):
    return render(request, 'blog_auth/profile_page.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('blog:home')
            else:
                messages.error(request, 'Invalid login or password')
                return redirect('blog_auth:login')

        # GET
        error_message = request.session.pop('error_message', None)

    return render(request, 'blog_auth/login_page.html', {'error_message': error_message})


def logout_page(request):
    logout(request)
    return redirect('blog:home')


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = UserCreationForm()
    return render(request, 'blog_auth/signup_page.html', {'form': form})
