from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    brand = models.TextField(blank=True)
    size_fit = models.TextField(blank=True)
    look_after_me = models.TextField(blank=True)
    about_me = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"Image for {self.product.name}"
