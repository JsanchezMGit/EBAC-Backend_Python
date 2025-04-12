from django.db import models

from cart.models import Cart

from product.models import Product

class Order(models.Model):

 cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

 total = models.DecimalField(max_digits=10, decimal_places=2)

 created_at = models.DateTimeField(auto_now_add=True)