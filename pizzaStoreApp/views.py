from django.shortcuts import render, get_object_or_404
from .models import *


def about_page(request):
    return render(request, 'about.html')


def home_page(request):
    if request.method == 'POST':
        print(request.POST)
        pizza_id = dict(request.POST).get('pizza')[0]
        try:
            quantity = PizzaQuantity.objects.get(pizza_id=pizza_id)
            quantity.quantity += 1
            quantity.save()
        except:
            quantity = PizzaQuantity.objects.create()
            quantity.pizza_id = pizza_id
            quantity.quantity = 1
            quantity.save()
    pizza = Pizza.objects.all()
    context = {'pizza': pizza}
    return render(request, 'home.html', context)


def cart_page(request):
    if request.method == 'POST':
        total_price = 0
        print(request.POST)
        pizzaQuantity = PizzaQuantity.objects.all()
        data = dict(request.POST)

        order = Order.objects.create()

        order.street, order.house, order.entrance, order.floor, order.room, order.name, order.surname, order.paymentMethod, order.phoneNumber = \
        data.get('street')[0], data.get('house')[0], data.get('entrance')[0], data.get('floor')[0], data.get('room')[0], \
        data.get('name')[0], data.get('surname')[0], data.get('payment')[0], data.get('phone-number')[0]
        total_pizzas = ''
        for i in pizzaQuantity:
            pizzaName = Pizza.objects.get(id=i.pizza.id).name
            total_price += i.pizza.price * i.quantity
            total_pizzas += f'{pizzaName}  ({i.quantity}шт.) —  {i.pizza.price * i.quantity} BYN, \n'
        order.totalPrice = round(total_price, 2)
        order.pizza = total_pizzas
        order.save()
        PizzaQuantity.objects.all().delete()

    pizza_quantity = PizzaQuantity.objects.all()
    pizza = Pizza.objects.all()

    context = {'quantity': pizza_quantity, 'pizza': pizza}

    return render(request, 'cart.html', context)
