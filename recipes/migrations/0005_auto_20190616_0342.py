# Generated by Django 2.2.2 on 2019-06-16 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_post_favorite_fruit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorite_fruit',
        ),
        migrations.AddField(
            model_name='post',
            name='Diet',
            field=models.CharField(choices=[('raw', 'Raw'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('other', 'Other')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
