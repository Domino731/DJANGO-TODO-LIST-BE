from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, default="FOO")
    content = models.TextField(blank=True, null=True, default="FOO")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    @property
    def get_discount(self):
        return '199'

    @property
    def get_year(self):
        return '1999'

    @property
    def get_country(self):
        return 'Germany'
