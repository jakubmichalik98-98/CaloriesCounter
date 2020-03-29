from django.shortcuts import render
from .forms import PersonalForm, AdvancedMealForm
from django.http import HttpResponseRedirect


def get_personal_form(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/diets/mealform/')

    else:
        form = PersonalForm()

    return render(request, 'diets/personal.html', {'form': form})


def get_meal_form(request):
    if request.method == "POST":
        meal_form = AdvancedMealForm(request.POST)
        if meal_form.is_valid():
            # return HttpResponseRedirect('/uzupelnic/')
            pass
    else:
        meal_form = AdvancedMealForm()

    return render(request, 'diets/meal.html', {'meal_form': meal_form})