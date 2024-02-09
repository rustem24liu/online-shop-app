from django.urls import path
from online_shop.views.product_views import  products_view, ProductDetailView, product_delete_view, product_update_view

urlpatterns = [
    path('', products_view, name='products_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', product_update_view, name='product_update'),
    path('delete/<int:pk>', product_delete_view, name='product_delete'),
]
