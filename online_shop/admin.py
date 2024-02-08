from django.contrib import admin

from online_shop.models import Product, Category


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'category', 'img']
    list_filter = ['price', 'category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'price', 'category', 'img', 'created_at']
    readonly = ['created_at']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['name', 'description', 'category_img']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)