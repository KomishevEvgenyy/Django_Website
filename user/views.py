from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm
from .models import User, Profile


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
                    LoginView(request, user)
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
            profile = Profile.objects.create(user=new_user)  # создание пустого профиля после регистрации
            return render(request, 'user/register_done.html', {'new_user': new_user})  # переход на страницу после
            # успешной регистрации
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/register.html', {'user_form': user_form})  # переход на страницу регистрации


def images(request):
    return HttpResponse('Images')


def people(request):
    return HttpResponse('people')


@login_required
# пароверка прохода аутентификации. Если прошел представление выполниться, если нет перенаправит на страницу входа
def dashboard(request):
    # return LoginView
    return render(request, 'user/dashboard.html')


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        # хранения данных встроенной модели User и ProfileEditForm для хранения дополнительных данных профиля
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # если True сохраняем обе формы для обновления соответствующего объекта в базе данных.
            user_form.save()
            profile_form.save()
            return render(request, 'user/edit_done.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'user/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})
