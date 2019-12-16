from django.contrib import admin
from django.urls import path

from . import views

app_name = 'product'
urlpatterns = [
    path('', views.index, name="index"),

    #path('category/<int:id>/', views.categories, name='category'),
    path('all_brands/', views.all_brands, name='all_brands'),  # url который выводит все бренды в категории
    #path('<int:brand_id>/', views.detail, name='name'),
]