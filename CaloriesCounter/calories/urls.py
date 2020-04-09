from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('meal/', views.get_meal, name="get_name"),
    path('question/', views.get_question, name="get_question"),
    path('delete_calories/<int:i>', views.delete_calories),
]
