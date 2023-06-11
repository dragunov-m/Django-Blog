from django.db import models
from blog.models import Post, Author
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'Comment Author: {self.author} / Post ID: {self.post_id}'
