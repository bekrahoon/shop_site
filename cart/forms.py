from django import forms
from .models import Cart, Product


class CartAddForm(forms.ModelForm):
    quantity = forms.IntegerField(
        min_value=1,
        label="Количество",
        widget=forms.NumberInput(attrs={"class": "form-control", "step": 1}),
    )

    class Meta:
        model = Cart
        fields = ["quantity"]

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop("product", None)
        super().__init__(*args, **kwargs)

    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]

        if self.product and self.product.stock < quantity:
            raise forms.ValidationError(
                f"Доступно только {self.product.stock} шт. на складе."
            )
        return quantity
