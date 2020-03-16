from django import forms


class MealForm(forms.Form):
    meal = forms.CharField(label="Meal", max_length=200)
    category = forms.CharField(label="Category", max_length=200)
    kcal_quantity = forms.IntegerField(label="Kcal Quantity")
