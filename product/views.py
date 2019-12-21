from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Categories, Brand, Goods


def all_categories(request):
    output_categories = Categories.objects.order_by('id')
    return render(request, 'product/page_categories.html', {'output_categories': output_categories})


def all_brands(request, num=1):
    # return HttpResponse('страница с брендами')
    output_brand = Brand.objects.order_by("id")
    return render(request, 'product/page_brands.html', {'output_brand': output_brand})


def all_goods(request, brand_id):
    output_goods = Brand.objects.all()
    return render(request, 'product/page_brands.html', {'output_goods': output_goods})



