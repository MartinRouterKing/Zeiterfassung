from datetime import date
from django.db import models
from django.contrib.auth.models import User
from calender.models import CalendarEvent
from datetime import datetime
from django.db.models import Sum
from django.core.exceptions import ObjectDoesNotExist


class User_limitations(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    limit = models.IntegerField(("Beschränkung in Montaten"))
    
    def __str__(self):
        return self.limit

class Workingtime(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    workingtime = models.IntegerField(("Arbeitszeit pro Woche"), blank=True)

    def __int__(self):
        return self.user_id

    def get_wk_employ_month(self):
        current_date = datetime.today()
        current_year= current_date.year
        current_month = current_date.month
        wk_per_month = CalendarEvent.objects.filter(start__year=current_year,
                                                    start__month=current_month,
                                                    user_id=self.user_id).aggregate(Sum('hours'))
        try:
            wk_time = self.workingtime
        except ObjectDoesNotExist:
            wk_time = 0

        wk_max = wk_time * 4.35

        if wk_per_month['hours__sum'] is None:
            wk_per_month['hours__sum'] = 0

        wk_per_month_prec = round(float(wk_per_month['hours__sum']) * 100 / wk_max,2)


        wk_max = "{0}".format(str(round(wk_max, 1) if wk_max % 1 else int(wk_max)))
        wk_per_month['hours__sum'] = "{0}".format(str(round(wk_per_month['hours__sum'], 1) if wk_per_month['hours__sum'] % 1 else int(wk_per_month['hours__sum'])))

        wk_result = {
            'wk_month_perc': wk_per_month_prec,
            'wk_per_month': wk_per_month['hours__sum'],
            'wk_max': wk_max}

        return wk_result


class Categorie(models.Model):
    cat = models.CharField(("Typ"),max_length=200)

    def __str__(self):
        return self.cat


class KategorieElement(models.Model):
    kat_element = models.CharField(("Element"), max_length=200, default=None)

    def __str__(self):
        return self.kat_element

class Kategorie(models.Model):
    kategorie = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.kategorie

class Calc_Choices(models.Model):
    calc = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.calc

class Element(models.Model):
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    wie = models.TextField(max_length=100, default=None, null=True)
    obj = models.TextField( max_length=100, default=None, null=True)
    element = models.ForeignKey(KategorieElement, on_delete=models.CASCADE, default=None)
    calc = models.ForeignKey(Calc_Choices, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.element)

class ElementTOKat(models.Model):
    katgroup = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    ele = models.ForeignKey(KategorieElement, on_delete=models.CASCADE)

class FavoriteElement(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fav_element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id)

