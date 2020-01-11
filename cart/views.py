from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from product.models import Goods
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """
        Представление для добавления товаров в корзину или обновляет количества для существующих товаров

        Декоратор require_POST используется чтобы разрешить только POST запросы поскольку это представление изменит
        данные.
        В качестве параметра представление получает ID товара. После извлечения екземпляра продукта с заданным ID
        проверяем с помощью формы CartAddProductForm. Если форма валидна то добавляем или обновляем товар в корзине.
    """

    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        #  если форма валидна то мы или добавляем или обновляем товары в корзине
        cd = form.cleaned_data
        cart.add(goods=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')
    #  url cart_detail это наша корзина где будет отображаться товар.


def cart_remove(request, product_id):
    """
        Предствление для удаление товаров из корзины. Получает id продукта в качестве параметра
    """
    cart = Cart(request)
    product = get_object_or_404(Goods, id=product_id)
    #  извлекаем екземпляр продукта с заданным id
    cart.remove(product)
    # удаляем товар из корзины
    return redirect('cart:detail')


def cart_detail(request):
    """
       Представление для отображение корзины и её товаров. Показывает текущее состояние корзины.
    """
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})



