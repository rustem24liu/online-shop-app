from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from online_shop.forms import CategoryForm, ProductForm
from online_shop.models import Category, Product, Bookmark

def category_list_view(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'category/list.html', {'categories': categories})


def category_update_view(request, *args, **kwargs):
    category = get_object_or_404(Category, pk=kwargs.get('pk'))

    if request.method == "GET":
        form = CategoryForm(
            initial={
                'name': category.name,
                'description': category.description,
                'category_img': category.category_img
            }
        )
        return render(request, 'category/update.html', context={'form': form, 'category': category})
    elif request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            if 'category_img' in request.FILES:
                category.category_img = form.cleaned_data['category_img']
            category.save()
            return redirect('category_detail', pk=category.pk)
        else:
            return render(request, 'category/update.html', context={'form': form, 'category': category})

def category_delete_view(request, *args, **kwargs):
    category = get_object_or_404(Category, pk=kwargs.get('pk'))
    if request.method == "GET":
        return render(request, 'category/delete.html', context={'category': category})
    elif request.method == "POST":
        category.delete()
        return redirect('category_list')

class CategoryDetailView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        return render(request, 'category/view.html', context={'form': form, 'category': category})
