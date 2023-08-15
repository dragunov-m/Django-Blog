from rest_framework import serializers
from blog.models import Post
from blog.models import Comment


class BlogCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class BlogPageSerializer(serializers.ModelSerializer):
    comments = BlogCommentsSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
