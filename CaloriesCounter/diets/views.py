from django.shortcuts import render
from .forms import PersonalForm, AdvancedMealForm, ReduceForm
from django.http import HttpResponseRedirect
from .models import AdvancedMeal, ReduceKcal
from .services import AdvancedModelDataService, PersonalFormDataService, CountingReducedCaloriesService, \
    SummaryCaloriesService


def get_personal_form(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            request.session['data_dict'] = form.cleaned_data
            return HttpResponseRedirect('/diets/advanced/')

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


def reduce_form(request):
    if request.method == "POST":
        reduced_form = ReduceForm(request.POST)
        if reduced_form.is_valid():
            activity = reduced_form.cleaned_data["activity"]
            hours = reduced_form.cleaned_data["hours"]
            reduce_kcal = ReduceKcal(activity=activity, hours=hours)
            reduce_kcal.save()
            return HttpResponseRedirect("/diets/advanced/")

    else:
        reduced_form = ReduceForm()

    return render(request, "diets/reduced.html", {"reduced_form": reduced_form})


def advanced_info(request):
    todays_objects = AdvancedMeal.today_objects.all()
    todays_reduce = ReduceKcal.today_objects.all()
    counting_reduce = CountingReducedCaloriesService(todays_reduce)
    service_meal = AdvancedModelDataService(todays_objects)
    eaten_kcal_sum = service_meal.sum_of_kcal()
    eaten_proteins_sum = service_meal.sum_of_proteins()
    eaten_fats_sum = service_meal.sum_of_fats()
    eaten_carbohydrates_sum = service_meal.sum_of_carbohydrates()
    reduced_calories = counting_reduce.get_reduced_kcal()

    data_dict = request.session["data_dict"]
    service_personal_form = PersonalFormDataService(data_dict)

    summary_of_kcal = SummaryCaloriesService(eaten_kcal_sum, counting_reduce.get_reduced_kcal()).get_summary_of_kcal()

    ppm = service_personal_form.get_ppm()
    required_proteins = service_personal_form.required_proteins()
    required_fats = service_personal_form.required_fats()
    required_carbohydrates = service_personal_form.required_carbohydrates()

    context = {"ppm": ppm, 'kcal_sum': eaten_kcal_sum, 'proteins_sum': eaten_proteins_sum,
               'carbohydrates_sum': eaten_carbohydrates_sum,
               'fats_sum': eaten_fats_sum, "required_fats": required_fats,
               "required_carbohydrates": required_carbohydrates,
               "required_proteins": required_proteins, "reduced_calories": reduced_calories, "summary": summary_of_kcal}

    return render(request, "diets/advanced.html", context)
