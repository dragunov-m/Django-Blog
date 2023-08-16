from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=50, blank=False, unique=True)
    avatar = models.ImageField(default='blog_auth/profile_pics/avatar.webp',
                               upload_to='blog_auth/profile_pics/')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
