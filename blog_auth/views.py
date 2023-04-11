from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


@login_required(login_url='blog_auth:login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.author)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile is updated.')
            return redirect('blog_auth:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.author)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'blog_auth/profile_page.html', context)


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
    if request.user.is_authenticated:
        return redirect('blog:home')
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:home')
        else:
            form = UserRegistrationForm()
    return render(request, 'blog_auth/signup_page.html', {'form': form})
