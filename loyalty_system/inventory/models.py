from django.db import models
from product.models import Product

# Create your models here.
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory of {self.product.name}"