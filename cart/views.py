from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

import product
from product.models import Goods
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    #  добавляет товары в корзину или обновляет количество для существующих товаров
    cart = Cart(request)
    product_id = get_object_or_404(Goods, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        #  если форма валидна то мы или добавляем или обновляем товары в корзине
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')
    #  url cart_detail это наша корзина где будет отображаться товар.


def cart_remove(request, product_id):
    #  удаление товаров из корзины. Получает id продукта в качестве параметра
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    #  извлекаем екземпляр продукта с заданным id
    cart.remove(product)
    # удаляем товар из корзины
    return redirect('cart:detail')


def cart_detail(request):
    #  отображение корзины и её товаров. Показывает текущее состояние корзины.
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})



