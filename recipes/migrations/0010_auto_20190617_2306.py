# Generated by Django 2.2.2 on 2019-06-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]
