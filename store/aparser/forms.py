from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'address', 'link')
        widgets = {'name': forms.TextInput, 'address': forms.TextInput}

