from django.contrib import admin

from .models import Flat, Complaint

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['address', 'town', 'town_district']
    readonly_fields = ["created_at"]
    list_display = ['address','price','construction_year','town','new_building']
    list_editable = ['new_building']
    list_filter = ['new_building']

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields =['complainant', 'flat']
    list_display = ['complainant', 'flat', 'text']