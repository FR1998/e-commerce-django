from django.shortcuts import render
from django.core.paginator import Paginator
from product_catalogue.models import *


def display_product(request):
    products = Product.objects.all()
    category = Category.objects.all()
    
    active_products = Paginator(products,8)
    page = request.GET.get("page")
    active_page = active_products.get_page(page)
    
    context = {"products": active_page, "categories": category}
        
    return render(request, "display_product.html", context)


def display_with_category(request,category_id):
    sort_by = request.GET.get("sort", "name")
    category = Category.objects.get(id=category_id) 
    products = Product.objects.filter(category=category).order_by(sort_by) 
    
    active_products = Paginator(products,6)
    page = request.GET.get("page")
    active_page = active_products.get_page(page)
    
    context = {"products": active_page}      
    
    return render(request, "display_category_wise.html", context)
    

def display_detail_product(request, id):
    product = Product.objects.filter(id=id)
    context = {"products": product}    
    
    return render(request, "display_detail_product.html", context)


def search_products(request):
    query_name = request.GET.get("query", None)
    products = Product.objects.filter(name__icontains=query_name)
    
    active_products = Paginator(products,12)
    page = request.GET.get("page")
    active_page = active_products.get_page(page)           # I will try to dry this pagination code tomorrow
    
    context = {"products": active_page} 
    
    return render(request, "search_product.html", context)

