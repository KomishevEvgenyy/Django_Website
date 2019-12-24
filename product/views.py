from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Categories, Brand, Goods


def product_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    products = Goods.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,

                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Goods,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'product/detail.html',
                  {'product': product})
