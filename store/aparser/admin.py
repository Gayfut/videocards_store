from django.contrib import admin
from .forms import ProductForm
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """register products in admin panel"""
    list_display = ('name', 'price', 'address', 'link')
    form = ProductForm
