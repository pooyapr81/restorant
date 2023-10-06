# Generated by Django 4.2.5 on 2023-09-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_food_photo_alter_food_pup_date_alter_food_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('B', 'breakfast'), ('L', 'lunch'), ('D', 'diner'), ('DR', 'drink')], default='D', max_length=10),
        ),
    ]
