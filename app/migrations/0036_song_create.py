# Generated by Django 4.2.1 on 2023-06-17 10:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0035_remove_createplaylist_playlistname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='create',
            field=models.ManyToManyField(blank=True, default=None, related_name='create', to=settings.AUTH_USER_MODEL),
        ),
    ]
