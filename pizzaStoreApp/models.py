from django.db import models


class Pizza(models.Model):
    name = models.TextField(max_length=60)
    price = models.FloatField(max_length=60)
    description = models.TextField(max_length=200)
    picture = models.ImageField()
    weight = models.TextField(max_length=60)

    def __str__(self):
        return self.name


class PizzaQuantity(models.Model):
    pizza = models.ForeignKey(Pizza, max_length=60, unique=True, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)

class Order(models.Model):
    pizza = models.TextField()
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    house = models.CharField(max_length=60)
    entrance = models.CharField(max_length=60)
    floor = models.CharField(max_length=60)
    room = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=60)
    totalPrice = models.FloatField(null=True)
    paymentMethod = models.CharField(max_length=60)






