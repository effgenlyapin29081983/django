from django.urls import path

from admins.views import index, UserListView, UserCreateView, UserUpdateView, UserDeleteView, ProductListView, \
     ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCategoryDeleteView, ProductCategoryUpdateView, \
     ProductCategoryCreateView, ProductCategoryListView


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('products/', ProductListView.as_view(), name='admin_products'),
    path('product-categories/', ProductCategoryListView.as_view(), name='admin_product_categories'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('products-create/', ProductCreateView.as_view(), name='admin_products_create'),
    path('product-category-create/', ProductCategoryCreateView.as_view(), name='admin_product_category_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('products-update/<int:pk>/', ProductUpdateView.as_view(), name='admin_products_update'),
    path('product-category-update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='admin_product_category_update'),
    path('users-delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products-delete/<int:pk>/', ProductDeleteView.as_view(), name='admin_products_delete'),
    path('product-category-delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='admin_product_category_delete'),
]