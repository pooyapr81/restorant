# Generated by Django 4.2.5 on 2023-09-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_food_type_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('breakfast', 'breakfast'), ('lunch', 'lunch'), ('dinner', 'dinner'), ('drinks', 'drinks')], default='dinner', max_length=10),
        ),
    ]
