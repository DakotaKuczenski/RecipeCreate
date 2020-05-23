# Generated by Django 2.2.2 on 2019-08-09 02:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0020_auto_20190807_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='follow',
            field=models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
