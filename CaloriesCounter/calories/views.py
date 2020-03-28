from .models import Meal
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MealForm
from datetime import date
import json


def index(request):
    meal_list = []
    today_date = date.today()
    kcal_sum = 0

    for my_meal in Meal.objects.all():
        if my_meal.date_added == today_date and my_meal.users == request.user.username:
            meal_list.append(my_meal)
            kcal_sum += my_meal.kcal_quantity
    context = {'meal_list': meal_list, 'kcal_sum': kcal_sum}
    return render(request, 'calories/index.html', context)


def get_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            category = form.cleaned_data["category"]
            kcal_quantity = form.cleaned_data["kcal_quantity"]
            meal = Meal(name=name, category=category, users=request.user.username, kcal_quantity=kcal_quantity)
            meal.save()
            return HttpResponseRedirect("/calories/")

    else:
        form = MealForm()

    with open("C:/ProjektyDjango/CaloriesCounter/calories.json", "r") as file:
        calories = json.load(file)

    return render(request, "calories/name.html", {"form": form, "calories": calories})


def get_question(request):
    return render(request, 'calories/question.html')
