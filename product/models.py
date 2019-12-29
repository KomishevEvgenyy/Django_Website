from django.db import models
from django.urls import reverse
from django.conf import settings


class Categories(models.Model):  # моделька для создания категории товаров
    name = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Конвенция для получения URL-адреса данного объекта.
        return reverse('product:product_list_by_category',
                       args=[self.slug])


class Brand(models.Model):  # моделька для создания брендов товаров
    name = models.CharField(' Name brand', max_length=256)  # поле для хранения именни бренда
    slug = models.SlugField(max_length=256, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class Goods(models.Model):  # моделька для создания товара
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)
    # поле для выбора категории, related_name которое будем использовать для отношения от связаного обьекта
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)  # поле для выбора бренда
    name = models.CharField(' Name model', max_length=256)  # поле для хранения имени модели товара
    slug = models.SlugField(max_length=200, db_index=True)  # Алиас продукта(его URL)
    text = models.TextField('description', blank=True)  # поле для хранения описания
    price = models.DecimalField(max_digits=10, decimal_places=2)  # поле для хранения денежных сумм товара
    stock = models.PositiveIntegerField()  # для хранения остатков продукта
    available = models.BooleanField(default=True)  # показывает в наличии продукт или нет.
    # Можно включать или отключать продукт в каталоге.
    image = models.ImageField(upload_to='products/%Y/%m/%d')  # поле для хранения картинки
    created = models.DateTimeField(auto_now_add=True)  # будет хранить дату когда создан обьект
    updated = models.DateTimeField(auto_now=True)  # время последнего обновления товара

    class Meta:
        ordering = ('name', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return f'{self.category}: {self.name}: {self.picture}'

    def get_absolute_url(self):  # Конвенция для получения URL-адреса данного объекта.
        return reverse('product:product_detail',
                       args=[self.id, self.slug])




