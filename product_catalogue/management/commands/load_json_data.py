import json
import re

from django.core.management.base import BaseCommand
from decimal import Decimal
from product_catalogue.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('product_catalogue/data/clothes.json') as product_readings:
            product_detail = json.load(product_readings)

            for product_attributes in product_detail:
                product_specifications = product_attributes.get("product_info", {})
                category_name = product_specifications.get("Product Category", "Product does not have a category")
                
                category = Category.objects.get_or_create(name=category_name)

                product_price = product_attributes["product_price"]
                product_price = Decimal(re.sub(r'[^\d.]', '', product_price))

                product = Product.objects.create(
                    name=product_attributes["product_name"],
                    price=product_price,
                    code=product_attributes["product_code"],
                    category=category 
                )
                
                product.category = category
                product.save()
                
                product.product_specifications = {category.name: product_specifications.get("Product Category")}
                product.save()

                for image_url in product_attributes["product_images"]:
                    image = ProductImage(product=product, image=image_url)
                    image.save()

                for name, value in product_specifications.items():
                    feature = ProductFeature(product=product, name=name, value=value)
                    feature.save()

