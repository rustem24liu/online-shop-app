from django.urls import path
from online_shop.views.bookmark_views import \
    add_to_bookmark, bookmarks_list_view, bookmark_delete_view

urlpatterns = [
    path('add/<int:pk>', add_to_bookmark, name='add_to_bookmark'),
    path('list', bookmarks_list_view, name='bookmark_list'),
    path('delete/<int:pk>', bookmark_delete_view, name='bookmark_delete')
]
