from django.contrib.auth.models import User
from tracking.models import Categorie, Element
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = ['cat']

class WieForm(forms.Form):
    class Meta:
        model = Element
        field = ['wie']

class ObjForm(forms.Form):
    class Meta:
        model = Element
        field = ['obj']


