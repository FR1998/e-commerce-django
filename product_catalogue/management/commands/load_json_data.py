import json
import re

from django.core.management.base import BaseCommand
from decimal import Decimal
from product_catalogue.models import *


class Command(BaseCommand):
     def handle(self):
        with open('product_catalogue/data/clothes.json') as product_readings:
            product_values = json.load(product_readings)

            for item in product_values:
                product_info = item.get("product_info", {})
                category_name = product_info.get("Product Category", "Product does not have a category")
                
                categories = Category.objects.filter(name=category_name)

                if categories.exists():
                    category = categories.first() 
                else:
                    category = Category(name=category_name)
                    category.save()

                product_price = item.get("product_price", "")
            
                if isinstance(product_price, str):
                    product_price = Decimal(re.sub(r'[^\d.]', '', product_price))

                product = Product(
                    name=item["product_name"],
                    price=product_price,
                    code=item["product_code"],
                    category=category
                )
                
                product.save()
                product.product_info = {category.name: product_info.get("Product Category")}
                product.save()

                for image_urls in item["product_images"]:
                    image_url = ProductImage(product=product, image=image_urls)
                    image_url.save()

                for one_feature_key, one_feature_value in product_info.items():
                    feature = ProductFeature(product=product, name=one_feature_key, value=one_feature_value)
                    feature.save()
        
