from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(default='blog_auth/profile_pics/avatar.webp',
                               upload_to='blog_auth/profile_pics/')

    def __str__(self):
        return self.username
