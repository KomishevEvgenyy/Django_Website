from django.contrib import admin
from django.contrib.auth import login, logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.password_validation import password_changed
from django.urls import path
from django.conf.urls import url

from . import views
from .views import register, user_login, dashboard

app_name = 'user'
urlpatterns = [
    path('', views.index, name="index"),
    url(r'^register/$', register, name='register'),
    # url(r'^login/$', user_login, name='login'),

    url(r'^login/$', login, name='login'),  # вход пользователя
    url(r'^logout/$', logout, name='logout'),  # вызод пользователя
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    # выход пользователя и перенаправление его на страницу входа
    url(r'^$', dashboard, name='dashboard'),  # переход после аутентификации

    # url(r'^password-change/$', password_changed, name='password_change'),  # отображает
    # форму для изминения пароля
    # url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    # страница после успешного изминения пароля

    # url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),  # сброс пароля
    # url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # сообщение о сбросе пароля и отправка его на email
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views'
    #     '.password_reset_confirm',
    #     name='password_reset_confirm'),  # установка пароля
    # url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
    #     name='password_reset_complete'),  # успешный сброс пароля
]
