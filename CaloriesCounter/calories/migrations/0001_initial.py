# Generated by Django 3.0.4 on 2020-03-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('users', models.CharField(max_length=200)),
                ('kcal_quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
