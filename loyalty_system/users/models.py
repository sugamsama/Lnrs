from django.db import models

# Create your models here.
class CustomUser(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100, choices=[('customer', 'Customer'), ('admin', 'Admin')], default='customer')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    