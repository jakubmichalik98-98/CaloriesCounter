# Generated by Django 3.0.4 on 2020-03-26 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0002_meal_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
