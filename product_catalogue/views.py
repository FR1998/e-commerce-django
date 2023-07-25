from django.shortcuts import render
from product_catalogue.models import *
from product_catalogue.pagination import get_pagination


def product_listing(request):
    products = Product.objects.all()
    category = Category.objects.all()
    
    active_page = get_pagination(request, products)

    context = {"products": active_page, "categories": category}
        
    return render(request, "index.html", context)


def list_products_with_category(request, category_id):
    sort_by = request.GET.get("sort", "name")
    category = Category.objects.get(id=category_id) 
    products = Product.objects.filter(category=category).order_by(sort_by) 
    
    active_page = get_pagination(request, products)
    
    context = {"products": active_page, "sorting":sort_by}      
    
    return render(request, "listing_with_category.html", context)
    

def get_product_details(request, id):
    product = Product.objects.filter(id=id)
    context = {"products": product}    
    
    return render(request, "details.html", context)


def search_products(request):
    query_name = request.GET.get("query", None)
    products = Product.objects.filter(name__icontains=query_name)
    
    active_page = get_pagination(request,products)    
    
    context = {"products": active_page, "query":query_name} 
    
    return render(request, "search_product.html", context)

