from django.urls import path, include
from rest_framework import routers
from .views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
