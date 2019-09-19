from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="category_img", blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop:category-by-category', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_main = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_1 = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_2 = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_3 = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_4 = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_5 = models.ImageField(upload_to="product_img", blank=True, null=True)
    image_6 = models.ImageField(upload_to="product_img", blank=True, null=True)
    stock = models.IntegerField()
    is_activated = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:product-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name