# Generated by Django 3.0.3 on 2020-03-06 05:56

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_image',
            field=models.ImageField(blank=True, upload_to=blog.models.Post.user_directory_path),
        ),
    ]
