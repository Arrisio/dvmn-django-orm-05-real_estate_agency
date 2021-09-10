from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ["address", "town", "town_district"]
    readonly_fields = ["created_at"]
    list_display = [
        "address",
        "price",
        "construction_year",
        "town",
        "new_building",
    ]
    list_editable = ["new_building"]
    list_filter = ["new_building"]
    raw_id_fields = ["liked_by"]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["complainant", "flat"]
    list_display = ["complainant", "flat", "text"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat"]
    list_display = ["name"]
