# Generated by Django 3.2.18 on 2023-03-05 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20230305_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='featured_image',
        ),
    ]