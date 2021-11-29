from django.contrib import admin

from .models import *

admin.site.site_header = 'PIZZA ADMINISTRATION'

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'totalPrice', 'paymentMethod')


