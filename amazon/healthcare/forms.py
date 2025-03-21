from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'stock']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'product_image/*'})
        }