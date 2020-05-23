# Generated by Django 2.2.2 on 2019-06-16 03:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20190616_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Diet',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('raw', 'Raw'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('other', 'Other')], max_length=26),
        ),
    ]