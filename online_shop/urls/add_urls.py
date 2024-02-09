from django.urls import path
from online_shop.views.add_views import add, product_create_view, category_create_view

urlpatterns = [
    path('', add, name='add'),
    path('category/', category_create_view, name='add_category'),
    path('product/', product_create_view, name='add_product'),
]
