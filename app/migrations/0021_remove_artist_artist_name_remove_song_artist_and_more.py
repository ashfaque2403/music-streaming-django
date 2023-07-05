# Generated by Django 4.2.1 on 2023-06-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_rename_artist_name_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.AddField(
            model_name='artist',
            name='artists_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artist_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]