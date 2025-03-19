from django.db import models
from users.models import CustomUser

# Create your models here.
class LoyaltyProgram(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.name} has {self.points} points"