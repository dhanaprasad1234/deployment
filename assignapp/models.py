from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Name = models.CharField(max_length=50, null=True, blank=True, default='Default Name')
    Description = models.TextField()
    Price = models.DecimalField(max_digits=64, decimal_places=2)
    Created_at = models.DateTimeField(auto_now_add=True)