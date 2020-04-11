from django.shortcuts import render
from .forms import PersonalForm, AdvancedMealForm, ReduceForm
from django.http import HttpResponseRedirect
from .models import AdvancedMeal, ReduceKcal
from .services.services import AdvancedModelDataService, PersonalFormDataService, CountingReducedCaloriesService, \
    SummaryCaloriesService
from .services.week_services import WeekMealsDataService
from .services.execute_services import execute_advanced_meal_service, execute_personal_data_services, \
    execute_week_data_service
from django.http import JsonResponse


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
    service_meal = AdvancedModelDataService(todays_objects, login_user)
    advanced_meal_dict = execute_advanced_meal_service(service_meal)
    counting_reduce = CountingReducedCaloriesService(todays_reduce, login_user)
    reduced_calories = counting_reduce.get_reduced_kcal()
    data_dict = request.session["data_dict"]
    service_personal_form = PersonalFormDataService(data_dict)
    summary_of_kcal = SummaryCaloriesService(service_meal.sum_of_kcal(),
                                             counting_reduce.get_reduced_kcal()).get_summary_of_kcal()
    personal_dict = execute_personal_data_services(service_personal_form)
    week_data_object = WeekMealsDataService(week_objects, login_user)
    week_dict = execute_week_data_service(week_data_object)
    view_dict = {"reduced_calories": reduced_calories, "summary": summary_of_kcal}
    context = {**view_dict, **week_dict, **personal_dict, **advanced_meal_dict}

    return render(request, "diets/advanced.html", context)


def get_calories_chart(request):
    return render(request, "diets/chart.html")


def calories_chart(request):
    week_objects = AdvancedMeal.week_objects.all()
    week_service = WeekMealsDataService(week_objects, request.user.username)
    week_data_dict = week_service.sum_each_day_calories()
    labels = [keys for keys in week_data_dict]
    data = [values for keys, values in week_data_dict.items()]

    return JsonResponse(data={'labels': labels, 'data': data})
