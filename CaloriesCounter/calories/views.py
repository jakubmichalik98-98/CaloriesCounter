from .models import Meal
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MealForm


def index(request):
    meal_list = []
    for my_meal in Meal.objects.all():
        if my_meal.users == "jakub":
            meal_list.append(my_meal)
    context = {'meal_list': meal_list}

    return render(request, 'calories/index.html', context)


def get_meal(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/calories/")

    else:
        form = MealForm()

    return render(request, "calories/name.html", {"form": form})




