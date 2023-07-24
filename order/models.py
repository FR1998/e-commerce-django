from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2)  
    order_placed_date = models.DateField(auto_now_add=True)
    shipping_address = models.TextField(blank=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey("product_catalogue.Product", on_delete=models.CASCADE, related_name="orders")
    
