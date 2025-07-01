from django.contrib import admin

from webapp.models import Product, Category

# Register your models here.
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    class ProductAdmin(admin.ModelAdmin):
        list_display = ('id', 'title', 'price', 'category', 'created_at')


admin.site.register(Product, ProductAdmin)
