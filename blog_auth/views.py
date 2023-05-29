from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# from blog.models import Author
User = get_user_model()


# class ProfilePage(LoginRequiredMixin, CreateView):
#     model = Author
#     form_class = ProfileUpdateForm
#     template_name = 'blog_auth/profile_page.html'
#     success_url = reverse_lazy('blog_auth:profile')
#     login_url = 'blog_auth:login'
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs
#
#     def form_valid(self, form):
#         u_form = UserUpdateForm(self.request.POST, instance=self.request.user)
#         p_form = form
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(self.request, f'Your profile is updated.')
#             return super().form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['u_form'] = UserUpdateForm(instance=self.request.user)
#         return context

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


# def login_page(request):
#     if request.user.is_authenticated:
#         return redirect('blog:home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'Welcome back, {user.username}!')
#                 return redirect('blog:home')
#             else:
#                 messages.error(request, 'Invalid login or password')
#                 return redirect('blog_auth:login')
#
#         # GET
#         error_message = request.session.pop('error_message', None)
#
#     return render(request, 'blog_auth/login_page.html', {'error_message': error_message})


class CustomLoginView(LoginView):
    template_name = 'blog_auth/login_page.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {self.request.user.username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid login or password')
        return super().form_invalid(form)


# def logout_page(request):
#     logout(request)
#     return redirect('blog:home')


class SignUp(CreateView):
    template_name = 'blog_auth/signup_page.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('blog:home')

    # def get(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect(self.get_success_url())
    #     else:
    #         return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


# def signup_page(request):
#     if request.user.is_authenticated:
#         return redirect('blog:home')
#     else:
#         if request.method == 'POST':
#             form = UserRegistrationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('blog:home')
#         else:
#             form = UserRegistrationForm()
#     return render(request, 'blog_auth/signup_page.html', {'form': form})
