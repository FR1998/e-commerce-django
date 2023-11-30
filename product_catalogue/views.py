from django.shortcuts import render
from django.views import View
from product_catalogue.models import *
from product_catalogue.pagination import get_pagination

# comment added for github
class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        categories = Category.objects.all()
    
        active_page = get_pagination(request, products)

        context = {"products":active_page, "categories":categories}
        
        return render(request, "index.html", context)
    

class CategoryProductsView(View):
    def get(self, request, category_id):
        sort_by = request.GET.get("sort", "name")
        category = Category.objects.get(id=category_id) 
        products = Product.objects.filter(category=category).order_by(sort_by) 
    
        active_page = get_pagination(request, products)
    
        context = {"products":active_page, "sorting":sort_by}      
    
        return render(request, "listing_with_category.html", context)
    
    
class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {"product":product}    
    
        return render(request, "details.html", context)


class SearchProductsView(View):
    def get(self, request):
        query_name = request.GET.get("query", None)
        products = Product.objects.filter(name__icontains=query_name)
        
        context = {"products": products, "query": query_name}
        
        return render(request, "search_product.html", context)
    
