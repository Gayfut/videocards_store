from django.db import models


class Product(models.Model):
    """model for product"""
    name = models.TextField(verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    address = models.TextField(verbose_name='Адрес')
    link = models.URLField(verbose_name='Ссылка', unique=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    """model for image"""
    link = models.URLField(verbose_name='Ссылка на изображение')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')