from django import forms
from .models import AdvancedMeal, ReduceKcal

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

ACTIVITY_CHOICES = [
    ("running", "Running"),
    ("boxing", "Boxing"),
    ("skiing", "Skiing"),
    ("basketball", "Basketball"),
    ("football", "Football"),
    ("volleyball", "Volleyball"),
]

TIME_CHOICES = [
    (1, "1 hour"),
    (2, "2 hours"),
    (3, "3 hours"),
    (4, "4 hours"),
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


class ReduceForm(forms.Form):
    activity = forms.CharField(label="Activity", widget=forms.RadioSelect(choices=ACTIVITY_CHOICES))
    hours = forms.IntegerField(label="Hours", widget=forms.RadioSelect(choices=TIME_CHOICES))

    class Meta:
        model = ReduceKcal
        fields = ["activity", "hours"]
