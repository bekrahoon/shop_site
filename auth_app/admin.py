from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Поля, которые будут отображаться в списке пользователей
    list_display = ("email", "username", "is_staff", "is_active")
    # Поля, которые можно использовать для фильтрации
    list_filter = ("is_staff", "is_active", "groups")
    # Поля, доступные при создании/редактировании пользователя
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    # Поля, которые отображаются при создании нового пользователя
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    # Поля, доступные для поиска
    search_fields = ("email", "username")
    # Поля, по которым будет выполняться сортировка
    ordering = ("email",)


# Регистрируем модель пользователя с кастомным админом
admin.site.register(CustomUser, CustomUserAdmin)
