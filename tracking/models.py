from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Workingtime(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    workingtime = models.IntegerField(("Arbeitszeit pro Woche"), blank=True)

    def __int__(self):
        return self.time

class Categorie(models.Model):
    cat = models.CharField(max_length=200)

    def __str__(self):
        return self.cat

class Wie(models.Model):
    wie = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.wie

class Obj(models.Model):
    obj = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.obj

class Element(models.Model):
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    wie = models.ForeignKey(Wie, on_delete=models.CASCADE, default=None)
    obj = models.ForeignKey(Obj, on_delete=models.CASCADE, default=None)
    element = models.CharField(max_length=200)

    def __str__(self):
        return self.element
