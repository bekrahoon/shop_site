from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product
from typing import Dict, Any
from django.db.models import Q


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


class SearchResultsView(View):
    template_name = "shop/search_results.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        query = request.GET.get("q", "")
        category_id = request.GET.get("category_id")  # Получаем ID категории из запроса

        products = (
            Product.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            if query
            else Product.objects.all()
        )

        # Фильтруем по категории, если указано category_id
        if category_id:
            products = products.filter(category_id=category_id)

        # Сортировка по цене (опционально)
        products = products.order_by("price")

        categories = Category.objects.all()
        context: Dict[str, Any] = {
            "query": query,
            "products": products,
            "categories": categories,
            "category_id": category_id,
        }

        return render(request, self.template_name, context)
