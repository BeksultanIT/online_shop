from django.urls import path

from webapp.views import index, products_add, product_details, categories_add, categories_view, category_edit_view, \
    category_delete

urlpatterns = [
    path('', index, name='index'),
    path('products/', index, name='index'),
    path('products/add/', products_add, name='products_add' ),
    path('product/<int:pk>/', product_details, name='product_details' ),
    path('categories/add/', categories_add, name='categories_add'),
    path('categories/', categories_view, name='categories_view'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit'),
    path('categories/<int:pk>/delete/', category_delete, name='category_delete'),
]