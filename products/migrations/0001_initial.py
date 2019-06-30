# Generated by Django 2.2 on 2019-05-09 16:04
# flake8: noqa
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nutrition_grade', models.CharField(max_length=1)),
                ('url', models.CharField(max_length=255)),
                ('store', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=140)),
                ('thumb_link', models.CharField(max_length=255)),
                ('diet_link', models.CharField(max_length=255)),
            ],
        ),
    ]
