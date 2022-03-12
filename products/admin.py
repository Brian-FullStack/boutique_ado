from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    '''
    Customize the admin to make it easier
    to manage the products.
    Order the products by sku
    '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    '''
    Customize the category admin
    '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
