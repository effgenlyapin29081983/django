from users.forms import UserRegistrationForm, UserProfileForm
from products.forms import UpdateProductForm, CreateProductForm, CreateProductCategoryForm, UpdateProductCategoryForm
from django import forms

from users.models import User
from products.models import Product, ProductCategory


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'birthday', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class CreateAdminProductForm(CreateProductForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class UpdateAdminProductForm(UpdateProductForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')


class CreateAdminProductCategoryForm(CreateProductCategoryForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class UpdateAdminProductCategoryForm(UpdateProductCategoryForm):

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')