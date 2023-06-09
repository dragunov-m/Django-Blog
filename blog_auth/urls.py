from django.urls import path
from .views import SignUp, CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'blog_auth'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
]
