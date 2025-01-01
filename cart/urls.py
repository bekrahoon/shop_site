from django.urls import path
from .views import AddToCartView, RemoveFromCartView, CartView, UpdateCartView

urlpatterns = [
    path("cart/add/<int:product_id>/", AddToCartView.as_view(), name="add_to_cart"),
    path(
        "update-cart/<int:cart_item_id>/", UpdateCartView.as_view(), name="update_cart"
    ),
    path(
        "cart/remove/<int:cart_item_id>/",
        RemoveFromCartView.as_view(),
        name="remove_from_cart",
    ),
    path("cart/", CartView.as_view(), name="cart_view"),
]
