from django.db import models
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['created']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_activated = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product