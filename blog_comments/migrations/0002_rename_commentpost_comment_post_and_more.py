# Generated by Django 4.2 on 2023-04-25 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='CommentPost',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]