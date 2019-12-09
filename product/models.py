from django.db import models
from django.conf import settings


class Categories(models.Model):  # моделька для создания категории товаров
    name_categories = models.CharField("Name categories", max_length=256)

    def __str__(self):
        return self.name_categories


class Brand(models.Model):  # моделька для создания брендов товаров
    name_brand = models.CharField(' Name brand', max_length=256)  # поле для хранения именни бренда

    def __str__(self):
        return self.name_brand


class ObjectForCategories(models.Model):  # моделька для создания товара
    add_categories = models.ForeignKey('Categories', on_delete=models.CASCADE)  # поле для выбора категории
    add_brand = models.ForeignKey('Brand', on_delete=models.CASCADE)  # поле для выбора бренда
    object_model = models.CharField(' Name model', max_length=256)  # поле для хранения имени модели товара
    object_text = models.TextField('description')  # поле для хранения описания
    object_price = models.CharField(max_length=256)  # поле для хранения цены товара
    object_picture = models.ImageField(upload_to='')  # поле для хранения картинки

    def __str__(self):
        return self.object_model  # как вернуть название бренд в модельку обьектов




