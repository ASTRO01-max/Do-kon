from django.shortcuts import render
from .models import Category, Product, Inventory
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView


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

class ProductDeleteView(DeleteView):
    model = Product
    fields = ['product_name', 'product_stock', 'deleted_at', 'deleted_by']
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class ProductInventoryView(CreateView):
    model = Inventory
    fields = ['product', 'stock']
    template_name = 'products/product_inventory.html'
    success_url = reverse_lazy('home')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['category', 'name', 'real_price', 'price', 'expiration_data', 'description', 'barcode']
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('home')
