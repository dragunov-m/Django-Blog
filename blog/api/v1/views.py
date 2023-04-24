from django.forms import model_to_dict
from blog.models import Post
from rest_framework.response import Response
from rest_framework.views import APIView


class BlogPageAPI(APIView):

    def get(self, request):
        lst = Post.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Post.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            author_id=request.data['author_id'],
        )
        return Response({'post': model_to_dict(post_new)})