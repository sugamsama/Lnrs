from django.db import models
from django.utils.timezone import now

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock_quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default="Uncategorized")
    created_at = models.DateTimeField(default=now)  

    def __str__(self):
        return self.name
