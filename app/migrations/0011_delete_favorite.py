# Generated by Django 4.2.1 on 2023-05-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_song_favorited_by_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
