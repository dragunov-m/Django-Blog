from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('blog:home')
    else:
        error = 'Invalid login or password'
    return render(request, '', {'error': error})


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
    return render(request, '', {'form': form})
