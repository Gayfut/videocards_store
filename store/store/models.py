from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    img_links = models.URLField()
    link = models.URLField()