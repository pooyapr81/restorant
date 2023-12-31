# Generated by Django 4.2.5 on 2023-09-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50, verbose_name='توضیحات')),
                ('rate', models.IntegerField(verbose_name='امتیاز')),
                ('price', models.IntegerField()),
                ('time', models.IntegerField()),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='foods/')),
            ],
        ),
    ]
