from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def product_category(request, c_slug=None):
    category_page = None
    products = None
    if c_slug != None:
        category_page = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=category_page, is_activated=True)
    else:
        products = Product.objects.all().filter(is_activated=True)

    context = {'products': products, 'category': category_page}
    return render(request, "shop/category.html", context)

def product_detail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {'product': product}
    return render(request, "shop/product_detail.html", context)
