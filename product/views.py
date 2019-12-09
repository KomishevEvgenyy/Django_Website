from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Categories, Brand, ObjectForCategories


def index(request):
    return HttpResponse('views приложения product')


def all_categories(request):
    output_categories = Categories.objects.order_by('name_categories')
    return render(request, 'product/page_categories.html', {'output_categories': output_categories})


def all_brands(request):
    # return HttpResponse('страница с брендами')
    output_brand = Brand.objects.order_by("name_brand")
    return render(request, 'product/page_brands.html', {'output_brand': output_brand})

# def detail(request, brand_id):
# try:
# a = Brand.objects.get(id=brand_id)
# return render(request, 'product/page_brands.html', {'product': a})
# except:
# raise Http404('Категории не найдено')


# Create your views here.
