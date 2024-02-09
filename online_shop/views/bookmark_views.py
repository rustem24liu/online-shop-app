from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from online_shop.forms import CategoryForm, ProductForm
from online_shop.models import Category, Product, Bookmark


# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def add_to_bookmark(request, *args, **kwargs):
    product = get_object_or_404(Product, pk = kwargs.get('pk'))
    print('1 -> ', product)
    # return redirect('home_page')
    if request.method == 'GET':
        return render(request, 'bookmark/view.html', context={'product':product})
    elif request.method == "POST":
        new_bookmark = Bookmark.objects.create(
            product = product
        )
        new_bookmark.save()
        return redirect('bookmark_list')

def bookmarks_list_view(request, *args, **kwargs):
    product = Bookmark.objects.all()
    print(product)
    return render(request, 'bookmark/list.html', context={'products':product})

def bookmark_delete_view(request, *args, **kwargs):
    product = get_object_or_404(Bookmark, pk = kwargs.get('pk'))
    if request.method == 'POST':
        product.delete()
        return redirect('bookmark_list')
    elif request.method == "GET":
        return render(request, 'bookmark/delete.html', context={'product':product})


