from django import forms
from django.forms import widgets

from online_shop.models import Category


# class CategoryForm(forms.Form):

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name', widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the Categody'}))
    description = forms.CharField(max_length=500, required=False, label='Description', widget=widgets.Textarea(attrs={'class': 'form-control', 'placeholder':'Description', 'rows':'5'}))

    category_img = forms.ImageField(required=False, label='Image', widget=widgets.ClearableFileInput(attrs={'class': 'form-control', 'placeholder':'Your image'}))


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Name', widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the product'}))
    description = forms.CharField(max_length=500, required=False, label = 'Description', widget=widgets.Textarea(attrs={'class': 'form-control', 'placeholder':'Description', 'rows':'5'}))
    category = forms.CharField(max_length=200, required=True, label='Category', widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}))
    price = forms.DecimalField(required=True, label='Price', widget=widgets.NumberInput(attrs={'class': 'form-control', 'placeholder':'price'}))
    img = forms.ImageField(required=False, label='Image', widget=widgets.FileInput(attrs={'class': 'form-control'}))

