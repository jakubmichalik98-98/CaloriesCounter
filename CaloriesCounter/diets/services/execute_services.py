from .services import AdvancedModelDataService, PersonalFormDataService
from .week_services import WeekMealsDataService


def execute_advanced_meal_service(service_meal: AdvancedModelDataService):
    eaten_kcal_sum = service_meal.sum_of_kcal()
    eaten_proteins_sum = service_meal.sum_of_proteins()
    eaten_fats_sum = service_meal.sum_of_fats()
    eaten_carbohydrates_sum = service_meal.sum_of_carbohydrates()

    return {"sum_of_kcal": eaten_kcal_sum, "sum_of_proteins": eaten_proteins_sum,
            "sum_of_carbohydrates": eaten_carbohydrates_sum, "sum_of_fats": eaten_fats_sum}


def execute_personal_data_services(service_personal_form: PersonalFormDataService):
    ppm = service_personal_form.get_ppm()
    required_proteins = service_personal_form.required_proteins()
    required_fats = service_personal_form.required_fats()
    required_carbohydrates = service_personal_form.required_carbohydrates()

    return {"ppm": ppm, "required_proteins": required_proteins, "required_fats": required_fats,
            "required_carbohydrates":
                required_carbohydrates}


def execute_week_data_service(week_data_object: WeekMealsDataService):
    sum_week_kcal = week_data_object.sum_each_day_calories()
    avg_week_kcal = week_data_object.week_average_of_calories()
    max_week_kcal = week_data_object.get_the_biggest_value()
    min_week_kcal = week_data_object.get_the_smallest_value()
    most_frequent_category = week_data_object.get_most_often_category()

    return {"sum_week_kcal": sum_week_kcal, "avg_week_kcal": avg_week_kcal, "max_week_kcal": max_week_kcal,
            "min_week_kcal": min_week_kcal, "most_frequent_category": most_frequent_category}