from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Workingtime(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    workingtime = models.IntegerField(("Arbeitszeit pro Woche"), blank=True)

    def __int__(self):
        return self.user_id

class Categorie(models.Model):
    cat = models.CharField(("Type"),max_length=200)

    def __str__(self):
        return self.cat

class Wie(models.Model):
    wie = models.CharField(("Wirtscahftszweig"),max_length=200, default=None)

    def __str__(self):
        return self.wie

class Obj(models.Model):
    obj = models.CharField(("Objekt"),max_length=200, default=None)

    def __str__(self):
        return self.obj

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
    kategorie = models.ForeignKey(Kategorie, on_delete=models.CASCADE, default=None)
    wie = models.TextField(max_length=100, default=None)
    obj = models.TextField( max_length=100, default=None)
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

