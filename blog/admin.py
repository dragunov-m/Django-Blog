from django.contrib import admin
from .models import Categorie, Post, Comment

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Post)
admin.site.register(Comment)
