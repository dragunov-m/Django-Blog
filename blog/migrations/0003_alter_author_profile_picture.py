# Generated by Django 4.2 on 2023-04-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_category_slug_remove_category_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
