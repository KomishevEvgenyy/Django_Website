from django.db import models
from django.conf import settings


class Categories(models.Model):  # моделька для создания категории товаров
    name = models.CharField("Name categories", max_length=256)

    def __str__(self):
        return self.name


class Brand(models.Model):  # моделька для создания брендов товаров
    name = models.CharField(' Name brand', max_length=256)  # поле для хранения именни бренда

    def __str__(self):
        return self.name


class Goods(models.Model):  # моделька для создания товара
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)  # поле для выбора категории
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)  # поле для выбора бренда
    model = models.CharField(' Name model', max_length=256)  # поле для хранения имени модели товара
    text = models.TextField('description')  # поле для хранения описания
    price = models.CharField(max_length=256)  # поле для хранения цены товара
    picture = models.ImageField(upload_to='')  # поле для хранения картинки

    def __str__(self):
        return f'{self.categories}: {self.brand}: {self.model}: {self.picture}'




