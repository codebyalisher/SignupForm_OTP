from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='carts')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart {self.id} - {self.user.email}"

    def update_total(self):
        """Update total price of the cart based on the products"""
        self.total_price = sum([product.price for product in self.products.all()])
        self.save()
