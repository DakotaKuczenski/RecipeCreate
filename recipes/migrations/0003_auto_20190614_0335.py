# Generated by Django 2.2.2 on 2019-06-14 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_post_other'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='needed',
            new_name='Additional',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='other',
            new_name='Ingredients',
        ),
    ]
