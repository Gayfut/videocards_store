# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import Product, Image


class ProductView(TemplateView):
    template_name = "products/product.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "images": Image.objects.all(),
            "products": Product.objects.all()
        }
        return context