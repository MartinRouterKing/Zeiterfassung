from django.contrib import admin
from .models import Person
from tracking.models import Tracking, Categorie, Element, Workingtime
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from calender.models import CalendarEvent

@admin.register(Tracking)
class PersonAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['user_id', 'date', 'start_time', 'end_time', 'hours', 'categories', 'element']

@admin.register(Categorie)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['categories']

@admin.register(Element)
class ElementAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['categories', 'element']

admin.site.register(Person)
admin.site.register(Workingtime)
admin.site.register(CalendarEvent)
