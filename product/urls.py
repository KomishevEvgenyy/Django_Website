from django.contrib import admin
from django.urls import path

from .views import product_list, product_detail

app_name = 'product'
urlpatterns = [
    path('', product_list, name='product_list'),
    path('(<category_slug>[-/w]+)/', product_list, name='product_list_by_category'),
    path('(<id>/d+)/(<slug>[-/w]+)/', product_detail, name='product_detail'),

]