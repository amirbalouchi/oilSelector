from django.db import models
from .abstract_models import AbstractBaseModel

class Category(AbstractBaseModel):
    name = models.CharField(max_length=255)

class Product(AbstractBaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    external_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class ProductVariant(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product.name} - {self.sku}"

class RecommendedProduct(AbstractBaseModel):
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    capacity = models.CharField(max_length=255, blank=True, null=True)
    capacity_note = models.TextField(blank=True, null=True)
    recommendation_note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.car.year} {self.car.model.make} {self.car.model}"
