# Generated by Django 2.2.1 on 2019-05-17 14:05
# flake8: noqa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190513_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff'),
        ),
    ]
