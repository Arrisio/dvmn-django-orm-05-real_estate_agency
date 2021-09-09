from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town', 'town_district']
    readonly_fields = ["created_at"]

# admin.site.register(Flat)
