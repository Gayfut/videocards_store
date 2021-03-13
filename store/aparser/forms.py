from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    """form for product in admin panel"""
    class Meta:
        model = Product
        fields = ('name', 'price', 'address', 'link')
        widgets = {'name': forms.TextInput, 'address': forms.TextInput}

