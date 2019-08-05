from .models import Categorie, Element, Workingtime, Kategorie, KategorieElement, Calc_Choices, ElementTOKat,User_limitations
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from calender.models import CalendarEvent
from django.contrib.auth.models import User


@admin.register(User_limitations)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['user_id', 'limit']

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

@admin.register(ElementTOKat)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = ['katgroup', 'ele']


@admin.register(CalendarEvent)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = [
            'user_id',
            'event_id',
            'title',
            'type',
            'start',
            'hours',
            'end',
            'calc',
            'note',
            'all_day'
        ]

admin.site.unregister(User)

@admin.register(User)
class CategorieAdmin(ImportExportModelAdmin):
    class Meta:
        fields = [
            'id',
            'password',
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined'
            ]

admin.site.register(Workingtime)



