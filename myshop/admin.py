from django.contrib import admin
from .models import Product, Form

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')   # admin list columns
    search_fields = ('name',)                   # search box
    list_filter = ('price',)                    # filter by price

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')
    list_filter = ('submitted_at',)