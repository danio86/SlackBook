# Generated by Django 3.2.18 on 2023-03-05 19:28

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20230305_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
