from django.urls import path
from online_shop.views.category_views import  CategoryDetailView, category_update_view, \
    category_delete_view, category_list_view

urlpatterns = [
    path('', category_list_view, name='category_list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('update/<int:pk>', category_update_view, name='category_update'),
    path('delete/<int:pk>', category_delete_view, name='category_delete'),
]
