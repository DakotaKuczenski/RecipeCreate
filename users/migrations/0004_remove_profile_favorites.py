# Generated by Django 2.2.2 on 2019-08-07 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
    ]