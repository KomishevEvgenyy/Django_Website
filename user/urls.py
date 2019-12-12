from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from . import views


app_name = 'user'
urlpatterns = [
    path('', views.index, name="index"),
    path(r'^register/$', views.RegisterFormView.as_view()),
    path(r'^login/$', views.LoginFormView.as_view()),
    path(r'^logout/$', views.LogoutView.as_view())
]