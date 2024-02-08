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
    product_create_view
from source.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home_page'),
    path('category/', category_list_view, name='category_list'),
    path('products/', products_view, name='products_list'),
    path('add/', add, name='add'),
    path('add/category', category_create_view, name='add_category'),
    path('add/product', product_create_view, name='add_product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
