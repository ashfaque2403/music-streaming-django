# Generated by Django 4.2.1 on 2023-05-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_song_audio_link_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20),
        ),
    ]
