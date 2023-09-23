from django.contrib import admin
from .models import Sport


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    search_fields = ['name']
