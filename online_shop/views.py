from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from online_shop.forms import CategoryForm, ProductForm
from online_shop.models import Category, Product, Bookmark


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def category_list_view(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'category/list.html', {'categories': categories})


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', context={'products': products})


def add(request):
    return render(request, 'add.html')


def category_create_view(request):
    # print(request.GET)
    # print(request.POST)
    if request.method == "GET":
        form = CategoryForm()
        return render(request, 'category/create.html', context={'form': form})
    elif request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            new_category = Category.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category_img=form.cleaned_data['category_img'],
            )
            return redirect('category_list')
        else:
            return render(request, 'category/create.html', context={'form': form})


def product_create_view(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'products/create.html', context={'form': form, 'categories': Category.objects.all()})
    elif request.method == "POST":
        print("its POST")
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            category = Category.objects.get(pk=request.POST.get('category'))
            print(category)
            new_product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=category,
                price=form.cleaned_data['price'],
                img=form.cleaned_data['img'],
            )
            return redirect('products_list')
        else:
            return render(request, 'products/create.html', context={'form': form, 'categories': Category.objects.all()})


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


def product_update_view(request, *args, **kwargs):
    product = get_object_or_404(Product, pk=kwargs.get('pk'))

    if request.method == "GET":
        form = ProductForm(
            initial={
                'name': product.name,
                'description': product.description,
                'category': product.category,
                'price': product.price,
                'img': product.img,
            }
        )
        return render(request, 'products/update.html',
                      context={'form': form, 'product': product, 'categories': Category.objects.all()})
    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        print(form.as_p())
        if form.is_valid():
            category_id = form.cleaned_data['category']
            print(category_id, type(category_id))
            category = get_object_or_404(Category, pk = category_id)
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = category
            product.price = form.cleaned_data['price']
            if 'img' in request.FILES:
                product.img = request.FILES['img']
            product.save()
            return redirect('product_detail', pk=product.id)
        else:
            return render(request, 'products/update.html',
                          context={'form': form, 'product': product, 'categories': Category.objects.all()})

def product_delete_view(request, *args, **kwargs):
    product = get_object_or_404(Product, pk = kwargs.get('pk'))
    if request.method == 'GET':
        return render(request, 'products/delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('products_list')


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



class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        product = get_object_or_404(Product, pk=kwargs['pk'])
        return render(request, 'products/view.html', context={'product': product, 'form': form})


class CategoryDetailView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        category = get_object_or_404(Category, pk=kwargs.get('pk'))
        return render(request, 'category/view.html', context={'form': form, 'category': category})
