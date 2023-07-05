# Generated by Django 4.2.1 on 2023-05-23 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_song_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_title', models.CharField(max_length=50)),
                ('play_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('playlist_artist', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.playlist'),
        ),
    ]