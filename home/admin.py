from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Product Inventory"
admin.site.site_title = "Welcome to Product Inventory"
