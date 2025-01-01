from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from shop.models import Category
from .models import Product, Cart
from django.contrib.auth import get_user_model
from .forms import CartAddForm

User = get_user_model()


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.is_authenticated:
            messages.error(
                request, "Вы должны быть авторизованы для добавления в корзину."
            )
            return redirect("login")

        form = CartAddForm(request.POST, product=product)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]

            # Попытка создать или обновить товар в корзине
            cart_item, created = Cart.objects.get_or_create(
                user=request.user, product=product
            )

            if created:
                cart_item.quantity = quantity
            else:
                if cart_item.quantity + quantity <= product.stock:
                    cart_item.quantity += quantity
                else:
                    messages.error(
                        request,
                        f"Доступно только {product.stock - cart_item.quantity} шт.",
                    )
                    return redirect("product_detail", product_id=product.id)

            cart_item.save()
            product.stock -= quantity
            product.save()
            messages.success(request, f"{product.name} добавлен в корзину!")
        else:
            for error in form.errors.values():
                messages.error(request, error)

        return redirect("cart_view")


class RemoveFromCartView(View):
    def post(self, request, cart_item_id):
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
        product = cart_item.product

        # Увеличиваем количество товара на складе
        product.stock += cart_item.quantity
        product.save()

        # Удаляем товар из корзины
        cart_item.delete()
        messages.success(request, f"{product.name} удален из корзины.")

        return redirect("cart_view")


class CartView(View):
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
        categories = Category.objects.filter(parent__isnull=True)

        return render(
            request,
            "shop/cart.html",
            {
                "cart_items": cart_items,
                "total_price": total_price,
                "categories": categories,
            },
        )


class UpdateCartView(View):
    def post(self, request, cart_item_id):
        cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
        product = cart_item.product

        form = CartAddForm(request.POST, product=product)
        if form.is_valid():
            quantity = form.cleaned_data["quantity"]

            if quantity <= product.stock + cart_item.quantity:
                # Возвращаем остаток на склад
                product.stock += cart_item.quantity
                # Обновляем количество в корзине
                cart_item.quantity = quantity
                cart_item.save()

                # Уменьшаем остаток на складе
                product.stock -= quantity
                product.save()
                messages.success(
                    request,
                    f"Количество товара '{product.name}' успешно обновлено.",
                )
            else:
                messages.error(
                    request,
                    f"На складе доступно только {product.stock + cart_item.quantity} шт.",
                )
        else:
            for error in form.errors.values():
                messages.error(request, error)

        return redirect("cart_view")
