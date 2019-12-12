from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View

from .models import User


def index(request):
    return HttpResponse('views приложения user')


class RegisterFormView(FormView):  # регистрация пользователя
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "user/login/"
    template_name = "register.html"  # Шаблон, который будет использоваться при отображении представления.

    def form_valid(self, form):
        form.save()  # Создаём пользователя, если данные в форму были введены корректно.
        return super(RegisterFormView, self).form_valid(form)  # Вызываем метод базового класса form_valid


class LoginFormView(FormView):  # авторизация пользователя
    form_class = AuthenticationForm
    template_name = "login.html"  # Аналогично регистрации, только используем шаблон аутентификации.
    success_url = "/"  # В случае успеха перенаправим на главную.

    def form_valid(self, form):
        self.user = form.get_user()  # Получаем объект пользователя на основе введённых в форму данных.
        login(self.request, self.user)  # Выполняем аутентификацию пользователя.
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):  # выход из учетной записи
    def get(self, request):
        logout(request)  # Выполняем выход для пользователя, запросившего данное представление.
        return HttpResponseRedirect("/")  # После чего, перенаправляем пользователя на главную страницу.
