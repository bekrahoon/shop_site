from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View
from auth_app.forms import CustomRegisterForm, CustomLoginForm


class RegisterView(View):
    def get(self, request):
        form = CustomRegisterForm()
        return render(request, "auth_app/register.html", {"form": form})

    def post(self, request):
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Если вы изменяете данные перед сохранением
            user.save()  # Сохранение пользователя
            # Указываем backend для логина через строку пути
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            # Устанавливаем токен в куку
            response = redirect("index")

            messages.success(request, "Registration successful")
            return response

        return render(request, "auth_app/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = CustomLoginForm()
        return render(request, "auth_app/login.html", {"form": form})

    def post(self, request):
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Указываем backend для логина через строку пути
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            # Устанавливаем токен в куку
            response = redirect("index")

            messages.success(request, "Login successful")
            return response

        messages.error(request, "Login failed, please try again")
        return render(request, "auth_app/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        # Указываем вручную страницу для перенаправления после логаута
        return redirect("auth_app:login")
