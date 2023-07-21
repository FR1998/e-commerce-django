from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)    
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    code = models.CharField(max_length=20)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
            
    def __str__(self):
        return self.name
    

class ProductFeature(models.Model):
    feature = models.JSONField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="features")
    
    def __str__(self):
        return self.feature
    
    
class ProductImage(models.Model):
    image = models.ImageField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    
    def __str__(self):
        return self.image
    
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
      
class CartItem(models.Model):
    quantity = models.IntegerField(default=0)    
    payment = models.DecimalField(max_digits=10, decimal_places=2)  
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name="cart_items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    
    def __str__(self):
        return self.payment    
    
    
class Review(models.Model):
    star_rating = models.PositiveIntegerField(default=0, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    
    def __str__(self):
        return self.comment
    
