from django.urls import path
from .views import products_detail_view, products_view, category_list_view


app_name = "shop"

urlpatterns = [
    path('', products_view, name='products'),
    path('<slug:slug>/', products_detail_view, name='product_detail'),
    path('search/<slug:slug>/', category_list_view, name='category_list'),
]
