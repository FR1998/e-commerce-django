from django.core.paginator import Paginator


def get_pagination(request, products):
    active_products = Paginator(products,12)
    page = request.GET.get("page")
    active_page = active_products.get_page(page)
    
    return active_page

