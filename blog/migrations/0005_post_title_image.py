# Generated by Django 3.0.3 on 2020-03-06 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200305_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_image',
            field=models.ImageField(blank=True, upload_to='title-images'),
        ),
    ]
