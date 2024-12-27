from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from typing import Dict, Any


class IndexView(View):
    template_name = "shop/index.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        categories = Category.objects.filter(parent__isnull=True)
        context: Dict[str, Any] = {"categories": categories}
        return render(request, self.template_name, context)


class CategoryDetailView(View):
    template_name = "shop/category_detail.html"

    def get_category(self, category_id: int) -> Category:
        return get_object_or_404(Category, id=category_id)

    def get(self, request: HttpRequest, category_id: int) -> HttpResponse:
        category = self.get_category(category_id)
        products = category.products.all()
        context: Dict[str, Any] = {"category": category, "products": products}
        return render(request, self.template_name, context)


class ProductDetailView(View):
    template_name = "shop/product_detail.html"

    def get_product(self, product_id: int) -> Product:
        return get_object_or_404(Product, id=product_id)

    def get(self, request: HttpRequest, product_id: int) -> HttpResponse:
        product = self.get_product(product_id)
        context: Dict[str, Any] = {"product": product}
        return render(request, self.template_name, context)
