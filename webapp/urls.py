from django.urls import path

from webapp.views import index, products_add, product_details, categories_add

urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='index'),
    path('products/add/', products_add, name='products_add' ),
    path('product/<int:pk>/', product_details, name='product_details' ),
    path('categories/add/', categories_add, name='categories_add')
]