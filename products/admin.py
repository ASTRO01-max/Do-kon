from django.contrib import admin
from .models import Category, Product, Inventory

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Inventory)