from django.contrib import admin
from .models import House
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "smoking_allowed","address"]
    list_filter = ["price","smoking_allowed"]
    search_fields = ["address"]