# Generated by Django 3.2.9 on 2021-11-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaStoreApp', '0002_alter_pizzaquantity_pizza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='pizza_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
    ]
