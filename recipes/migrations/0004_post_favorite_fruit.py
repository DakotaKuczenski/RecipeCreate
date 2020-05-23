# Generated by Django 2.2.2 on 2019-06-16 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20190614_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite_fruit',
            field=models.CharField(choices=[('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]