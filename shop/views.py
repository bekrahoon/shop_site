from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
    categories = Category.objects.filter(parent__isnull=True)
    return render(request, "shop/index.html", {"categories": categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(
        request,
        "shop/category_detail.html",
        {"category": category, "products": products},
    )


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})
