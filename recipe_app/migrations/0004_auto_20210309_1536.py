# Generated by Django 3.1.6 on 2021-03-09 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0003_author_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='favorite',
            new_name='favorites',
        ),
    ]