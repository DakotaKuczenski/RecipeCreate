# Generated by Django 2.2.2 on 2019-08-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
