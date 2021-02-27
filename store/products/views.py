from django.views.generic import TemplateView

from products.models import Product, Image


class ProductView(TemplateView):
    template_name = "products/product.html"

    def get_context_data(self, *args, **kwargs):
        context = {
            "products": self.__get_products(),
        }
        return context

    @staticmethod
    def __get_products():
        products_without_images = Product.objects.all()
        products = []

        for product in products_without_images:
            _image = Image.objects.filter(product=product).first()
            _product = {"product": product, "image": _image}
            products.append(_product)

        return products
