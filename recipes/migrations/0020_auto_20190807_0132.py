# Generated by Django 2.2.2 on 2019-08-07 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_post_favorites'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='favorites',
            new_name='favorite',
        ),
    ]