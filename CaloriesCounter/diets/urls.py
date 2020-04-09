from django.urls import path
from . import views


urlpatterns = [
    path('personalform/', views.get_personal_form, name="personal_form"),
    path('mealform/', views.get_meal_form, name="meal_form"),
    path('advanced/', views.advanced_info, name="advanced"),
    path('reduceform/', views.reduce_form, name="reduce_form"),
    path('chart/', views.get_calories_chart, name="chart"),
    path('calories_chart/', views.calories_chart, name="calories-chart"),

]