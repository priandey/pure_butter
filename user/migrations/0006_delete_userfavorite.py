# Generated by Django 2.2.1 on 2019-05-22 17:32
# flake8: noqa
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190517_1627'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavorite',
        ),
    ]
