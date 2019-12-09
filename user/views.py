from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('views приложения user')

# Create your views here.
