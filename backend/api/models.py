from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True, default="Enter content here")
    price = models.DecimalField(max_digits=10, decimal_places=3, default=99.99)

    def __str__(self):
        self.title