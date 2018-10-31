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

class Element(models.Model):
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    element = models.CharField(max_length=200)

    def __str__(self):
        return self.element

class Tracking(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=date.today)
    start_time = models.TimeField(("Start Time"), blank=True, default=None, null=True)
    end_time = models.TimeField(("End Time"), blank=True, default=None, null=True)
    hours = models.TimeField(("Hours"), blank=True)
    categories = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    element = models.ForeignKey(Element, on_delete=models.SET_NULL, null=True)
    notiz = models.TextField('Notiz',blank=True, default=None, null=True)

    def __str__(self):
        return '{},{},{},{},{},{},{},{}'.format(self.user_id,
                                                self.date,
                                                self.start_time,
                                                self.end_time,
                                                self.hours,
                                                self.categories,
                                                self.element,
                                                self.notiz)

