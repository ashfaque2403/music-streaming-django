# Generated by Django 4.2.1 on 2023-05-27 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_favorite_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]