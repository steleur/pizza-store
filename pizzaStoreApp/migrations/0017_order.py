# Generated by Django 3.2.9 on 2021-11-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaStoreApp', '0016_alter_pizza_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('street', models.CharField(max_length=60)),
                ('house', models.CharField(max_length=60)),
                ('entrance', models.CharField(max_length=60)),
                ('floor', models.CharField(max_length=60)),
                ('room', models.CharField(max_length=60)),
                ('phoneNumber', models.CharField(max_length=60)),
                ('totalPrice', models.FloatField()),
                ('paymentMethod', models.CharField(max_length=60)),
                ('pizza', models.ManyToManyField(to='pizzaStoreApp.Pizza')),
            ],
        ),
    ]