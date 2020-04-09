from django.shortcuts import render
from .forms import PersonalForm, AdvancedMealForm, ReduceForm
from django.http import HttpResponseRedirect
from .models import AdvancedMeal, ReduceKcal
from .services.services import AdvancedModelDataService, PersonalFormDataService, CountingReducedCaloriesService, \
    SummaryCaloriesService
from .services.week_services import WeekMealsDataService


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
            reduce_kcal = ReduceKcal(activity=activity, hours=hours, users=request.user.username)
            reduce_kcal.save()
            return HttpResponseRedirect("/diets/advanced/")

    else:
        reduced_form = ReduceForm()

    return render(request, "diets/reduced.html", {"reduced_form": reduced_form})


def advanced_info(request):
    login_user = request.user.username

    todays_objects = AdvancedMeal.today_objects.all()
    todays_reduce = ReduceKcal.today_objects.all()
    week_objects = AdvancedMeal.week_objects.all()

    counting_reduce = CountingReducedCaloriesService(todays_reduce, login_user)
    service_meal = AdvancedModelDataService(todays_objects, login_user)
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

    week_data_object = WeekMealsDataService(week_objects, login_user)
    sum_week_kcal = week_data_object.sum_each_day_calories()
    avg_week_kcal = week_data_object.week_average_of_calories()
    max_week_kcal = week_data_object.get_the_biggest_value()
    min_week_kcal = week_data_object.get_the_smallest_value()
    most_frequent_category = week_data_object.get_most_often_category()

    context = {"ppm": ppm, 'kcal_sum': eaten_kcal_sum, 'proteins_sum': eaten_proteins_sum,
               'carbohydrates_sum': eaten_carbohydrates_sum,
               'fats_sum': eaten_fats_sum, "required_fats": required_fats,
               "required_carbohydrates": required_carbohydrates,
               "required_proteins": required_proteins, "reduced_calories": reduced_calories, "summary": summary_of_kcal,
               "sum_week_kcal": sum_week_kcal, "avg_week_kcal": avg_week_kcal, "max_week": max_week_kcal, "min_week":
               min_week_kcal, "most_frequent_category": most_frequent_category}

    return render(request, "diets/advanced.html", context)
