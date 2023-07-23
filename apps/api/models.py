from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteModel

# Create your models here.
class Brand(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    brand = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.brand

    class Meta:
        db_table = 'brand' 
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

class Product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product' 
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Buyouts(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    buyout_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"The user {self.user} bought the product: {self.product}"

    class Meta:
        db_table = 'buyout'
        verbose_name = 'Buyout'
        verbose_name_plural = 'Buyouts'