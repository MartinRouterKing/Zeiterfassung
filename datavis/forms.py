from django import forms

CHOICES=[('select1','select 1'),
         ('select2','select 2')]

class Choice(forms.Form):
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())