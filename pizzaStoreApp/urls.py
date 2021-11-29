

from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('cart', views.cart_page, name='cart')




]
