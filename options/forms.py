from bootstrap_datepicker_plus import TimePickerInput
from django import forms
from tracking.models import Element, Categorie, Workingtime, Kategorie, Calc_Choices,KategorieElement
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = {'name', 'username', 'password1', 'password2', 'email', 'is_superuser', 'first_name', 'last_name'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class CalcForm(forms.ModelForm):
    class Meta:
        model = Calc_Choices
        fields = ['calc']
        widgets = {
            'calc': forms.TextInput(attrs={'class': 'form-control'}),
        }

class calcchoiceform(forms.Form):
    choice = forms.ModelChoiceField(queryset=Calc_Choices.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class Worktimefrom(forms.ModelForm):
    class Meta:
        model = Workingtime
        fields = ['workingtime']
        widgets = {
            'workingtime': TimePickerInput()
        }

class Categorieform(forms.ModelForm):
    class Meta:
        model = Kategorie
        fields = ['kategorie']
        widgets = {
            'kategorie': forms.TextInput(attrs={'class': 'form-control'})
        }

class editcatchoiceform(forms.Form):
    choice = forms.ModelChoiceField(queryset=Kategorie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class editcatform(forms.ModelForm):
    class Meta:
        model = Kategorie
        fields = ['kategorie']
        widgets = {
            'kategorie': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Elementform(forms.ModelForm):
    class Meta:
        model = KategorieElement
        fields = ['kat_element']
        widgets = {
            'kat_element': forms.TextInput()
        }



class editelechoiceform(forms.Form):
      choice = forms.ModelChoiceField(queryset=KategorieElement.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class Choicefrom(forms.ModelForm):
    class Meta:
        model = Element
        fields = ['categories', 'element']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['element'].queryset = Element.objects.none()


        if 'categories' in self.data:
            try:
                categories_id = int(self.data.get('categories'))
                self.fields['element'].queryset = Element.objects.filter(categories_id=categories_id).order_by('element')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['element'].queryset = self.instance.categorie.element_set.order_by('element')


