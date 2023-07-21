from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)    
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=30, null=True)
    code = models.CharField(max_length=20)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
            
    def __str__(self):
        return self.name
    

class ProductFeature(models.Model):
    feature = models.JSONField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.feature
    
    
class ProductImage(models.Model):
    image = models.ImageField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image
    
    
class Cart(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through="CartItem")
    
    
    
class CartItem(models.Model):
    quantity = models.IntegerField(default=0)    
    payment = models.DecimalField(max_digits=10, decimal_places=2)  
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.payment    
    
    
class Review(models.Model):
    star_rating = models.PositiveBigIntegerField(default=0, blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
    
class Order(models.Model):
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2)  
    order_placed_date = models.DateField(auto_now_add=True)
    shipping_address = models.TextField(blank=False)
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    
