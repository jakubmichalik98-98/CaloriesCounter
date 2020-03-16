from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('meal', views.get_meal, name="get_name")
]