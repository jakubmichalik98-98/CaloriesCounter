from django import forms
from .models import Meal


class MealForm(forms.Form):
    name = forms.CharField(label="Meal", max_length=200)
    category = forms.CharField(label="Category", max_length=200)
    kcal_quantity = forms.IntegerField(label="Kcal Quantity")

    class Meta:
        model = Meal
        fields = ["name", "category", "users", "kcal_quantity"]
