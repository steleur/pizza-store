# Generated by Django 3.2.9 on 2021-11-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaStoreApp', '0005_alter_pizzaquantity_quantity'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.AddField(
            model_name='pizzaquantity',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizzaquantity',
            name='pizza',
            field=models.CharField(max_length=60),
        ),
    ]
