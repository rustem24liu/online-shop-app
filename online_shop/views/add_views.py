from django.shortcuts import render, redirect

from online_shop.forms import CategoryForm, ProductForm
from online_shop.models import Category, Product


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


