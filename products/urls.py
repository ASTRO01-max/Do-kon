from django.urls import path
from .views import home, ProductCreateView, ProductCategoryView, ProductInventoryView, ProductDeleteView
from .views import ProductDetailView, CategoryDetailView, ProductUpdateView

urlpatterns = [
    path('', home, name = 'home'),
    path('add/', ProductCreateView.as_view(), name = 'product_add'),
    path('add_category/', ProductCategoryView.as_view(), name = 'product_category'),
    path('add_inventory/', ProductInventoryView.as_view(), name = 'product_inventory'),
    path('delete/product/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]

