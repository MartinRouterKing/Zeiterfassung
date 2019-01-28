from bootstrap_datepicker_plus import TimePickerInput
from django import forms
from tracking.models import Element, Categorie, Workingtime, Kategorie, Calc_Choices, KategorieElement
from django.contrib.auth.models import User
from options.admin import UserCreationForm
from django import forms


class UsereditForm(forms.Form):
    username_pop = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    email_pop = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name_pop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name_pop = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    working_time_pop = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    is_superuser = forms.CheckboxInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'is_superuser')

class CalcForm(forms.ModelForm):
    class Meta:
        model = Calc_Choices
        fields = ['calc']
        widgets = {
            'calc': forms.TextInput(attrs={'class': 'form-control'}),
        }

class calcchoiceForm(forms.Form):
    choice = forms.ModelChoiceField(label='Kostenträger auswählen:', queryset=Calc_Choices.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

class editCalcForm(forms.Form):
    choice = forms.ModelChoiceField(label="Kostenträger auswählen:",required=True,queryset=Calc_Choices.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    edit = forms.CharField(label="Kostenträger ändern:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

class Worktimefrom(forms.ModelForm):
    class Meta:
        model = Workingtime
        fields = ['workingtime']
        widgets = {
            'workingtime': TimePickerInput()
        }

class Categorieform(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['cat']
        widgets = {
            'cat': forms.TextInput(attrs={'class': 'form-control'})
        }

class deletecatForm(forms.Form):
    choice = forms.ModelChoiceField(label="Typ auswählen:", queryset=Categorie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


class editcatForm(forms.Form):
    choice = forms.ModelChoiceField(label="Typ auswählen:", queryset=Categorie.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    edit = forms.CharField(label="Kostenträger ändern:",required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


class Categoriechoiceform(forms.Form):
    cat_choice = forms.ModelChoiceField(queryset=Categorie.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}),label='')

class Elementform(forms.ModelForm):
    class Meta:
        model = KategorieElement
        fields = ['kat_element']
        widgets = {
            'kat_element': forms.TextInput(attrs={'class': 'form-control'})
        }

class editelechoiceform(forms.Form):
      choice = forms.ModelChoiceField(label="Kategorie auswählen:", queryset=KategorieElement.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

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


