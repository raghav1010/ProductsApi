from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.


class Sale(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)

