"""
    Инициализация корзины

    class Cart позволяет управлять корзиной для покукок. С помощью обьекта request будет происходить инициализация.
    self.session = request.session - будет хранить текущую сесию, для доступа других методов класса Cart
    self.session.get(settings.CART_SESSION_ID) - получаем корзину с текущей сесии
    Если в сессии отсутствует корзина, то мы создадим сессию с пустой корзиной, установив пустой словарь в сессии.
    Наш словарь корзины будет использовать коды продуктов в качестве ключей и словарь с количеством и ценой в качестве
    значения для каждого ключа. Таким образом, мы можем гарантировать, что продукт не будет добавлен в корзину более
    одного раза; можно также упростить доступ к данным элементов корзины.
"""
from decimal import Decimal
from django.conf import settings

from product.models import Goods


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранение пустой корзины сеанса с пустм словарем
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, goods, quantity=1, update_quantity=False):
        """
            Добавление продукта в корзину или обновления его количества

            product: екземпляр Goods для добавления или обновления в корзине
            quantity: число для количетсва продуктов. По умолчанию = 1
            update_quantity: логическое значение, которое указывает, требуется ли обновление количества с заданным
            количеством (True), или же новое количество должно быть добавлено к существующему количеству (False)

        """
        product_id = str(goods.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(goods.price)}
            #  преобразование цены продукта из десятичного разделителя в строку, чтобы сериализовать его
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        #  сохранение в корзину сесии

    def save(self):
        # обновление сесии Cart
        self.session[settings.CART_SESSION_ID] = self.cart
        #  отменить сеанс как отмененный, чтобы убедиться что он сохранен
        self.session.modified = True
        #  после сохранения всех изменений в корзине помечает сесию как modefied

    def remove(self, goods):
        """
            Удаление товаров из корзины
        """
        product_id = str(goods.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
            Перебор элементов в корзине и получение продуктов из базы данных

            Данный метод извлекаем экземпляры продукта, присутствующие в корзине, чтобы включить их в номенклатуры
            корзины. Далее проходим по элементам корзины, преобразуя цену номенклатуры обратно в десятичное число
            и добавляя атрибут total_price к каждому элементу. После выполняется итерация по товарам в корзине.
        """
        product_ids = self.cart.keys()
        #  получение обьектов goods и добавление их в корзину
        products = Goods.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
            Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Метод который подсчитывает общую стоимость товаров в корзине
        """
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Метод который удаляет корзины из сесии
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True




