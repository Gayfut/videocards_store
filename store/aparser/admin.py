from django.contrib import admin
from .forms import ProductForm
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'address', 'link')
    form = ProductForm
