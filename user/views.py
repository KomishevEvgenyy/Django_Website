from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, LoginForm
from .models import User


def index(request):
    return HttpResponse('views приложения user')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # создаем екземпляр формы с отправленными данными
        if form.is_valid():  # проверка валидности формы
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])  # ищем пользователя в базе данных
            if user is not None:
                if user.is_active:  # если прошел аутентификацию то проверяем активен он или нет
                    login(request, user)
                    return HttpResponse('Authenticated successfully')  # сообщение о проходжении аутентификацию
                else:
                    return HttpResponse('Disabled account')  # аккаунт не активный
            else:
                return HttpResponse('Invalid login')  # неверный логин
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)  # Создания нового пользователя без сохранения
            new_user.set_password(user_form.cleaned_data['password'])  # установка пароля
            new_user.save()  # Сохранения пользователя
            return render(request, 'user/register_done.html', {'new_user': new_user})  # переход на страницу после
            # успешной регистрации
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'user_form': user_form})  # переход на страницу регистрации


@login_required  # пароверка прохода аутентификации. Если прошел представление выполниться, если нет перенаправит на
# страницу входа
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
