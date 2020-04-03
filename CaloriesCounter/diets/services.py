from .models import AdvancedMeal, ReduceKcal
from typing import Dict


class CountingReducedCaloriesService:
    def __init__(self, today_reduce: ReduceKcal.today_objects.all()):
        self.today_reduce = today_reduce
        self.kcal_dict = {
            'running': 750,
            'boxing': 592,
            'skiing': 420,
            'basketball': 510,
            'football': 555,
            'volleyball': 470,
        }
        self.activity_list = [obj.activity for obj in today_reduce]
        self.hours_list = [obj.hours for obj in today_reduce]
        self.reducted_sum = 0

    def get_reduced_kcal(self):
        return sum([self.kcal_dict[self.activity_list[index]] * self.hours_list[index] for index in
                    range(len(self.activity_list))])


class AdvancedModelDataService:
    def __init__(self, meal_model: AdvancedMeal.today_objects.all()):
        self.meal_model = meal_model

    def sum_of_proteins(self):
        return sum([meal.proteins for meal in self.meal_model])

    def sum_of_carbohydrates(self):
        return sum([meal.carbohydrates for meal in self.meal_model])

    def sum_of_fats(self):
        return sum([meal.fats for meal in self.meal_model])

    def sum_of_kcal(self):
        return sum([meal.kcal_quantity for meal in self.meal_model])


class PersonalFormDataService:
    def __init__(self, data: Dict):
        self.data = data

    def get_ppm(self):
        if self.data["gender"] == "Male" or self.data["gender"] == "male":
            return int(66 + 13.7 * self.data["weight"] + 5 * self.data["height"] - 6.76 * self.data["age"])
        else:
            return int(655 + 9.6 * self.data["weight"] + 1.8 * self.data["height"] - 4.7 * self.data["age"])

    def required_proteins(self):
        return int(1.2 * self.data["weight"])

    def required_carbohydrates(self):
        return int(3 * self.data["weight"])

    def required_fats(self):
        return int((0.3 * self.get_ppm()) / 9)


class SummaryCaloriesService:
    def __init__(self, sum_of_kcal: int, reduce_of_kcal: int):
        self.sum_of_kcal = sum_of_kcal
        self.reduce_of_kcal = reduce_of_kcal

    def get_summary_of_kcal(self):
        return self.sum_of_kcal - self.reduce_of_kcal
