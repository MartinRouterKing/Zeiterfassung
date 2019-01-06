from .models import Categorie, Element, Workingtime, Kategorie, KategorieElement, Calc_Choices
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


@admin.register(Calc_Choices)
class Calc_ChoicesAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['calc']

@admin.register(Kategorie)
class WieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['kategorie']

@admin.register(KategorieElement)
class KategorieElement(ImportExportModelAdmin):
    class Meta:
        fields = ['kat_element']

admin.site.register(Workingtime)
admin.site.register(CalendarEvent)
