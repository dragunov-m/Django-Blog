# Core Django
from django.contrib import admin

# blog app
from .models import Categorie, Post, Comment

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Comment)
