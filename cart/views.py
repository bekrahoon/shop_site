from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Убедитесь, что пользователь авторизован и существует
    if not request.user.is_authenticated:
        messages.error(request, "Вы должны быть авторизованы для добавления в корзину.")
        return redirect("login")

    # Попытка создать или обновить товар в корзине
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if product.stock > 0:
        if not created:
            if cart_item.quantity + 1 <= product.stock:
                cart_item.quantity += 1
                cart_item.save()
                product.stock -= 1
                product.save()
                messages.success(request, f"{product.name} добавлен в корзину!")
            else:
                messages.error(
                    request, f"На складе доступно только {product.stock} шт."
                )
        else:
            cart_item.quantity = 1
            cart_item.save()
            product.stock -= 1
            product.save()
            messages.success(request, f"{product.name} добавлен в корзину!")
    else:
        messages.error(request, "Товар закончился на складе.")

    return redirect("cart_view")


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    product = cart_item.product

    # Увеличиваем количество товара на складе
    product.stock += cart_item.quantity
    product.save()

    # Удаляем товар из корзины
    cart_item.delete()
    messages.success(request, f"{product.name} удален из корзины.")

    return redirect("cart_view")


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    return render(
        request,
        "shop/cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )
