from django.db import models
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=99.99)

    @property
    def sale_price(self):
        return self.price * Decimal("0.9")  ## 10% off

    def get_discounted_price(self, discount_percent):
        return float(self.price) * (1 - discount_percent / 100)

    def __str__(self):
        return self.title
    
