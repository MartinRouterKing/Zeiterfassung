from django.contrib.auth.models import User
from tracking.models import Categorie
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]


class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = ['cat']




