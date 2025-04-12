from django.db import models

from product.models import Product

class Cart(models.Model):

 user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

 products = models.ManyToManyField(Product)