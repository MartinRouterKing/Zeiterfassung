from .models import Tracking, Categorie, Element, Workingtime
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from calender.models import CalendarEvent


@admin.register(Categorie)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['categories']

@admin.register(Element)
class ElementAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['categories', 'element']

admin.site.register(Workingtime)
admin.site.register(CalendarEvent)
