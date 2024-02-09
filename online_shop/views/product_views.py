from urllib import request

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView

from online_shop.forms import CategoryForm, ProductForm
from online_shop.models import Category, Product, Bookmark


def products_view(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', context={'products': products})




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

class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        product = get_object_or_404(Product, pk=kwargs['pk'])
        return render(request, 'products/view.html', context={'product': product, 'form': form})
