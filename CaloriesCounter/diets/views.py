from django.shortcuts import render
from .forms import PersonalForm, AdvancedMealForm
from django.http import HttpResponseRedirect
from .models import AdvancedMeal
from .services import AdvancedModelDataService, PersonalFormDataService


def get_personal_form(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            request.session['data_dict'] = form.cleaned_data
            return HttpResponseRedirect('/diets/mealform/')

    else:
        form = PersonalForm()

    return render(request, 'diets/personal.html', {'form': form})


def get_meal_form(request):
    if request.method == "POST":
        meal_form = AdvancedMealForm(request.POST)
        if meal_form.is_valid():
            name = meal_form.cleaned_data["name"]
            proteins = meal_form.cleaned_data["proteins"]
            carbohydrates = meal_form.cleaned_data["carbohydrates"]
            fats = meal_form.cleaned_data["fats"]
            category = meal_form.cleaned_data["category"]
            kcal_quantity = meal_form.cleaned_data["kcal_quantity"]
            advanced_meal = AdvancedMeal(name=name, users=request.user.username, proteins=proteins,
                                         carbohydrates=carbohydrates, fats=fats, category=category,
                                         kcal_quantity=kcal_quantity)
            advanced_meal.save()
            return HttpResponseRedirect('/diets/advanced/')

    else:
        meal_form = AdvancedMealForm()

    return render(request, 'diets/meal.html', {'meal_form': meal_form})


def advanced_info(request):
    todays_objects = AdvancedMeal.today_objects.all()
    service_meal = AdvancedModelDataService(todays_objects)
    eaten_kcal_sum = service_meal.sum_of_kcal()
    eaten_proteins_sum = service_meal.sum_of_proteins()
    eaten_fats_sum = service_meal.sum_of_fats()
    eaten_carbohydrates_sum = service_meal.sum_of_carbohydrates()

    data_dict = request.session["data_dict"]
    service_personal_form = PersonalFormDataService(data_dict)

    ppm = service_personal_form.get_ppm()
    required_proteins = service_personal_form.required_proteins()
    required_fats = service_personal_form.required_fats()
    required_carbohydrates = service_personal_form.required_carbohydrates()

    context = {"ppm": ppm, 'kcal_sum': eaten_kcal_sum, 'proteins_sum': eaten_proteins_sum,
               'carbohydrates_sum': eaten_carbohydrates_sum,
               'fats_sum': eaten_fats_sum, "required_fats": required_fats,
               "required_carbohydrates": required_carbohydrates,
               "required_proteins": required_proteins}

    return render(request, "diets/advanced.html", context)
