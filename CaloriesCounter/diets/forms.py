from django import forms
from .models import AdvancedMeal

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]


class PersonalForm(forms.Form):
    weight = forms.IntegerField(label="Your Weight[kg]")
    height = forms.IntegerField(label="Your Height[cm]")
    age = forms.IntegerField(label="Your Age")
    gender = forms.CharField(label="Your Gender", widget=forms.RadioSelect(choices=GENDER_CHOICES))


class AdvancedMealForm(forms.Form):
    name = forms.CharField(label="Name")
    proteins = forms.IntegerField(label="Proteins[g]")
    carbohydrates = forms.IntegerField(label="Carbohydrates[g]")
    fats = forms.IntegerField(label="Fats[g]")
    category = forms.CharField(label="Category")
    kcal_quantity = forms.CharField(label="Kcal Quantity")

    class Meta:
        model = AdvancedMeal
        fields = ["name", "proteins", "carbohydrates", "fats",
                  "category", "kcal_quantity", ]


