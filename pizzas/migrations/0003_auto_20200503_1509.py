# Generated by Django 3.0.5 on 2020-05-03 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='date_add',
            new_name='date_added',
        ),
    ]