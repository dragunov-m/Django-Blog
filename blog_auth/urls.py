from django.urls import path
from .views import SignUp, LoginView, ProfileView
from django.contrib.auth.views import LogoutView

app_name = 'blog_auth'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
