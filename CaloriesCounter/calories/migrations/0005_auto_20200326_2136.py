# Generated by Django 3.0.4 on 2020-03-26 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0004_auto_20200326_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
