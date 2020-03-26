from django.db import models
from datetime import date


class Meal(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    users = models.CharField(max_length=200)
    kcal_quantity = models.IntegerField(default=0)
    date_added = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.name}"
