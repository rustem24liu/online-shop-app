from django.shortcuts import render, redirect

from online_shop.forms import CategoryForm
from online_shop.models import Category, Product


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
        form = CategoryForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            new_category = Category.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
            )
            return redirect('category_list')
        else:
            return render(request, 'category/create.html', context={'form': form})
