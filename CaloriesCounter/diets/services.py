from .models import AdvancedMeal
from typing import Dict


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
        return 1.2 * self.data["weight"]

    def required_carbohydrates(self):
        return 3 * self.data["weight"]

    def required_fats(self):
        return (0.3 * self.get_ppm()) / 9

