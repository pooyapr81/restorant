from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    search_fields = ('name', 'number', 'text')


admin.site.register(Contact, ContactAdmin)
