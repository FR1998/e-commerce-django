from django.shortcuts import render
from product_catalogue.models import *
import json
# Create your views here.

def display_product(request):
    with open('product_catalogue/data/clothes.json') as f:
        data = json.load(f)
        
        for item in data:
            for category in item["product_info"]:
                category = Category(name=category)
                category.save()
                
            product = Product(
                name=item["product_name"],
                price=item["product_price"],
                code=item["product_code"]
            )
            product.save()
            
            for image_url in item["product_images"]:
                images = ProductImage(product=product, image=image_url)
                images.save()
                
            for one_feature in item["product_info"]:
                features = ProductFeature(product=product, feature=one_feature)
                features.save()    
                 
    products = Product.objects.all()
    context = {"products": products}    
    return render(request, "display_product.html", context)

def display_detail_product(request, id):
    product = Product.objects.filter(id=id)
    context = {"products": product}    
    return render(request, "display_detail_product.html", context)

# def display_with_category(request,category):
#     # products = Product.objects.filter(product_features__category__category_name__icontains=category)
#     products = Product.objects.all()
#     context = {"products": products}    
#     return render(request, "display_category_wise.html", context)
    


#products.product_features_set.all() to access all features
#Category.objects.filter(category_name="Cotton").values() by id 
        