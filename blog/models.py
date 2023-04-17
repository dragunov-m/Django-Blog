from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='blog_auth/profile_pics/avatar.webp',
                                        upload_to='blog_auth/profile_pics/')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='blog/post_tbs/thumbnail.png', upload_to='blog/post_tbs/')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title
