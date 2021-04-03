from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from mainapp.models import Item

@admin.register(Item)
class ItemAdmin(ImportExportActionModelAdmin):
    list_display = ("id", "Date")