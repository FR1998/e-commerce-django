from django.db import models


class Order(models.Model):
    total_ammount = models.DecimalField(max_digits=10, decimal_places=2)  
    order_placed_date = models.DateField(auto_now_add=True)
    shipping_address = models.TextField(blank=False)
    
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey("product_catalogue.Product", on_delete=models.CASCADE, related_name="orders")
    
