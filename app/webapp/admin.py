from django.contrib import admin

from webapp.models.category import Category
from webapp.models.product import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'created_at')
    list_filter = ('id', 'description', 'created_at')
    search_fields = ('description', 'created_at')
    fields = ('id', 'description', 'created_at')
    readonly_fields = ('id', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'price', 'created_at')
    list_filter = ('id', 'name', 'category', 'price', 'created_at')
    search_fields = ('name', 'description', 'category', 'price', 'created_at')
    fields = ('id', 'name', 'description', 'category', 'price', 'created_at')
    readonly_fields = ('id', 'name', 'description', 'category')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
