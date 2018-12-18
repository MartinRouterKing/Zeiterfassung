from django import forms
from django.contrib.auth.models import User
from tracking.models import Categorie


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = ['cat']