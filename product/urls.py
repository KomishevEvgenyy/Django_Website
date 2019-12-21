from django.contrib import admin
from django.urls import path

from .views import all_brands, all_goods

app_name = 'product'
urlpatterns = [

    path('all_brands/<int:num>', all_brands, name='all_brands'),  # url который выводит все бренды в категории
    path('goods/<int:num>', all_goods, name='goods'),
]