from .models import Categorie, Element, Workingtime, Obj, Wie, FavoriteElement
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

@admin.register(Obj)
class ObjAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['obj']

@admin.register(Wie)
class WieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['wie']

@admin.register(FavoriteElement)
class FavoriteElementAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['user_id','fav_element']

admin.site.register(Workingtime)
admin.site.register(CalendarEvent)
