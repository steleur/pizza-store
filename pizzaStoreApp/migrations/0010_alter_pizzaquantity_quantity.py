# Generated by Django 3.2.9 on 2021-11-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaStoreApp', '0009_alter_pizzaquantity_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaquantity',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]