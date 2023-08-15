from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from .forms import UserRegistrationForm, ProfileUpdateForm
User = get_user_model()


class ProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'blog_auth/profile_page.html'
    success_url = reverse_lazy('blog_auth:profile')
    success_message = 'Your profile\'s updated'
    login_url = 'blog_auth:login'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        if password:
            self.object.set_password(password)
            self.object.save()
            update_session_auth_hash(self.request, self.object)
        else:
            self.object.save()
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = 'blog_auth/login_page.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Welcome back, {username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid login or password')
        return super().form_invalid(form)


class SignUp(CreateView):
    template_name = 'blog_auth/signup_page.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('blog:home')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog:home')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)
