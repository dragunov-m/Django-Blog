from rest_framework import viewsets
from blog.api.v1.serializers import BlogPageSerializer
from blog.models import Post


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogPageSerializer
