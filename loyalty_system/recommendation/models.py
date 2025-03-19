from django.db import models
from users.models import CustomUser
from product.models import Product

# Create your models here.
class Recommendation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    recommended_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reason = models.TextField()
    
    def __str__(self):
        return f"{self.user.name} recommended {self.product.name}"