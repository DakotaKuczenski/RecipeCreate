# Generated by Django 2.2.2 on 2019-06-21 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0017_auto_20190621_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Ingredients',
        ),
        migrations.AddField(
            model_name='post',
            name='Ingredients',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
