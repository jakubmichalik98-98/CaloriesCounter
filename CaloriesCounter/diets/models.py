from django.db import models
from datetime import date


class TodayAdvancedMealManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_added=date.today())


class AdvancedMeal(models.Model):
    name = models.CharField(max_length=200)
    users = models.CharField(max_length=200)
    proteins = models.IntegerField()
    carbohydrates = models.IntegerField()
    fats = models.IntegerField()
    category = models.CharField(max_length=200)
    kcal_quantity = models.IntegerField()
    date_added = models.DateField(default=date.today)

    objects = models.Manager()
    today_objects = TodayAdvancedMealManager()

    def __str__(self):
        return f"{self.name}"


class TodayReduceKcalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_added=date.today())


class ReduceKcal(models.Model):
    activity = models.CharField(max_length=200)
    hours = models.IntegerField(default=0)
    date_added = models.DateField(default=date.today)

    objects = models.Manager()
    today_objects = TodayReduceKcalManager()

    def __str__(self):
        return f"{self.activity}: {self.hours}"
