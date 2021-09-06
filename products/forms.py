from django import forms

from products.models import Product, ProductCategory


class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class CreateProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class UpdateProductCategoryForm(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')