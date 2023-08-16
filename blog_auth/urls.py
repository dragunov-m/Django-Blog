from django.urls import path
from .views import SignUp, Login, Profile
from django.contrib.auth.views import LogoutView

app_name = 'blog_auth'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', Profile.as_view(), name='profile'),
]
