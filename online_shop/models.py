from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category Name')

    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Description")

    category_img = models.ImageField(null=True, blank=True, upload_to='images/', verbose_name="category image")

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="product name")

    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="description of product")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, verbose_name="category", related_name="products")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date and time")

    price = models.DecimalField(max_length=500, null=False, blank=False, decimal_places=2, verbose_name="price", max_digits=100)

    img = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name="img")

    def __str__(self):
        return f"{self.name} {self.description[:10]} in {self.category} {self.price} {self.img}"

class Bookmark(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='bookmark product', related_name="bookmarks")

    def __str__(self):
        return f"{self.product}"