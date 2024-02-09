"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from online_shop.views import index_view, category_list_view, products_view, category_create_view, add, \
    product_create_view, ProductDetailView, CategoryDetailView, category_update_view, category_delete_view, \
    product_update_view, product_delete_view
from source.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home_page'),
    path('category/', category_list_view, name='category_list'),
    path('products/', products_view, name='products_list'),
    path('add/', add, name='add'),
    path('add/category', category_create_view, name='add_category'),
    path('add/product', product_create_view, name='add_product'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>', category_update_view, name='category_update'),
    path('category/delete/<int:pk>', category_delete_view, name='category_delete'),
    path('products/update/<int:pk>', product_update_view, name='product_update'),
    path('products/delete/<int:pk>', product_delete_view, name = 'product_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
