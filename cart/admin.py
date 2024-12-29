from django.contrib import admin
from .models import Cart


# Создаем кастомный класс администратора для модели Cart
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "quantity",
        "get_total_price",
    )  # поля для отображения в списке
    list_filter = ("user", "product")  # фильтрация по этим полям
    search_fields = (
        "user__username",
        "product__name",
    )  # поиск по имени пользователя и товару

    # Добавляем возможность редактирования поля `quantity` прямо в списке
    list_editable = ("quantity",)

    # Форматируем отображение общей стоимости (если нужно)
    def get_total_price(self, obj):
        return obj.get_total_price()

    get_total_price.short_description = "Total Price"  # Переименовываем столбец


# Регистрируем модель Cart и ее админку
admin.site.register(Cart, CartAdmin)
