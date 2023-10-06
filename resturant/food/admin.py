from django.contrib import admin
from .models import Food


# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'pup_date', 'rate', 'time', 'price')
    search_fields = ('name', 'description', 'pup_date', 'rate', 'price')
    list_filter = ('rate', 'pup_date', 'time', 'price')
    # prepopulated_fields = {'description': ('description',)}
    # raw_id_fields = ('description',)


admin.site.register(Food, FoodAdmin)
