from django.shortcuts import render
from .models import Category, Product, Inventory
from django.urls import reverse_lazy
from django.views.generic import CreateView

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'products/home.html', context)

class ProductCreateView(CreateView):
    model = Product
    fields = ['category', 'name', 'real_price', 'price', 'expiration_data', 'description', 'barcode']
    template_name = 'products/product_add.html'
    success_url = reverse_lazy('home')

class ProductCategoryView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'products/product_category.html'
    success_url = reverse_lazy('home')

class ProductInventoryView(CreateView):
    model = Inventory
    fields = ['product', 'stock']
    template_name = 'products/product_inventory.html'
    success_url = reverse_lazy('home')
