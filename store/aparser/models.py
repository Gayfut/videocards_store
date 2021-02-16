from django.db import models


class Image(models.Model):
    link = models.URLField(verbose_name='Ссылка на изображение')


class Product(models.Model):
    name = models.TextField(verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    address = models.TextField(verbose_name='Адрес')
    img_links = models.ManyToManyField(Image, verbose_name='Ссылки на изображения')
    link = models.URLField(verbose_name='Ссылка')
