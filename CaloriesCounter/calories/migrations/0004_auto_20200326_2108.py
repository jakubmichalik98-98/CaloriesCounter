# Generated by Django 3.0.4 on 2020-03-26 20:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0003_auto_20200326_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date_added',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
