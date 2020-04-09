from ..models import AdvancedMeal
import calendar
from .services import PersonalFormDataService


class WeekMealsDataService:
    def __init__(self, week_objects: AdvancedMeal.week_objects.all(), auth_user):
        self.week_objects = week_objects
        self.day_dict = {"Monday": 0,
                         "Tuesday": 0,
                         "Wednesday": 0,
                         "Thursday": 0,
                         "Friday": 0,
                         "Saturday": 0,
                         "Sunday": 0}
        self.auth_user = auth_user

    def sum_each_day_calories(self):
        for objects in self.week_objects:
            if objects.users == self.auth_user:
                self.day_dict[calendar.day_name[objects.date_added.weekday()]] += objects.kcal_quantity
        return self.day_dict

    def week_average_of_calories(self):
        return int(sum(values for keys, values in self.day_dict.items()) / 7)

    def get_the_biggest_value(self):
        max_value = max(self.day_dict.values())
        return max_value

    def get_the_smallest_value(self):
        min_value = min(self.day_dict.values())
        return min_value

    def get_most_often_category(self):
        week_objects_with_auth_user = [objects.category for objects in self.week_objects if
                                       objects.users == self.auth_user]
        if week_objects_with_auth_user:
            return max(set(week_objects_with_auth_user), key=week_objects_with_auth_user.count)
        else:
            return "You have eaten nothing last week"
