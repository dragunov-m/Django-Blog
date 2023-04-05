from django.urls import path, include
from . import views

app_name = 'blog_auth'
urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('signup/', views.signup_page, name='signup'),
]
