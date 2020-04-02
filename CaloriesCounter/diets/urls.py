from django.urls import path
from . import views


urlpatterns = [
    path('personalform/', views.get_personal_form, name="personal_form"),
    path('mealform/', views.get_meal_form, name="meal_form"),
    path('advanced/', views.advanced_info, name="advanced"),
]