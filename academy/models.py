from django.db import models
from django.contrib.auth.models import User


# Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
# True


# ProductImage
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
# True


# Comment
class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.product.name}"
# True


# Rating
class Rating(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
# True


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    full_text = models.TextField(max_length=200)
    date = models.DateTimeField('Дата публикаци')

    def __str__(self):
        return self.name
