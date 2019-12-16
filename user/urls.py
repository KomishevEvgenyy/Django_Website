from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.views import logout_then_login, LoginView, LogoutView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView, PasswordChangeView, \
    PasswordChangeDoneView
from django.contrib.auth.password_validation import password_changed
from django.urls import path

from . import views
from .views import register, user_login, dashboard, edit, images, people

app_name = 'user'
urlpatterns = [
    # path('', views.index, name="index"),
    path('', dashboard, name='dashboard'),
    # переход после аутентификации
    path('register/', register, name='register'),
    # регистрация пользователя

    path('login/', LoginView.as_view(redirect_field_name='all_categories.html'), name='login'),
    # вход пользователя
    path('logout/', LogoutView.as_view(), name='logout'),
    # выход пользователя
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
    # выход пользователя и перенаправление его на страницу входа
    path('edit/', edit, name='edit'),
    # изминение аккаунта

    path('password-change/form', PasswordChangeView.as_view(success_url='password_change_done'),
         name='password_change_form'),  # не переходит на страницу password_change_done????
    # отображает форму для изминения пароля
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # страница после успешного изминения пароля

    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    # сброс пароля
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # сообщение о сбросе пароля и отправка его на email
    path('password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z)/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # Ввод нового пароля при его востановлении
    path('password-reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # успешный сброс пароля

    path('images/', images, name='images'),
    path('people/', people, name='people'),
]
