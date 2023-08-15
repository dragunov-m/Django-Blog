from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
User = get_user_model()


class Categorie(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='blog/post_tbs/thumbnail.png', upload_to='blog/post_tbs/')
    categories = models.ManyToManyField(Categorie, blank=True)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'Comment Author: {self.author} / Post ID: {self.post_id}'
