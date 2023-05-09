"""Add_Cart_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    path('products/', products, name='products'),
    path('add_cart/<int:pk>/', add_cart, name='add_cart'),
    path('fetch_cart_items/', fetch_cart_items, name='fetch_cart_items'),
    path('delete_item/', delete_item, name='delete_item')


    

]
