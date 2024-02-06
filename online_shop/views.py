from django.shortcuts import render

from online_shop.models import Category


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


def category_list_view(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'category_list.html', {'categories': categories})