from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, default="UNKNOWN")
    content = models.TextField(blank=True, null=True, default="UNKNOWN")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
