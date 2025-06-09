from django.urls import path
from .views import home, ProductCreateView, ProductCategoryView, ProductInventoryView, ProductDeleteView, \
    ProductDetailView

urlpatterns = [
    path('', home, name = 'home'),
    path('add/', ProductCreateView.as_view(), name = 'product_add'),
    path('add_category/', ProductCategoryView.as_view(), name = 'product_category'),
    path('add_inventory/', ProductInventoryView.as_view(), name = 'product_inventory'),
    path('delete/product/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
