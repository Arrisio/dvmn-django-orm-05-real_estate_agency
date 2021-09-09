from django.contrib import admin

from .models import Flat

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town', 'town_district']
    readonly_fields = ["created_at"]
    list_display = ['address','price','construction_year','town','new_building']
    list_editable = ['new_building']
    list_filter = ['new_building']

# admin.site.register(Flat)
