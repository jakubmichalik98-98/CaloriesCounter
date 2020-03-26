from .models import Meal
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MealForm


def index(request):
    meal_list = []

    for my_meal in Meal.objects.all():
        if my_meal.users == request.user.username:
            meal_list.append(my_meal)
    context = {'meal_list': meal_list}

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

    return render(request, "calories/name.html", {"form": form})
