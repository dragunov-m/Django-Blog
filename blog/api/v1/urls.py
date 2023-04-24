from django.urls import path
from .views import BlogPageAPI

urlpatterns = [
    path('v1/blog/posts', BlogPageAPI.as_view()),
]
