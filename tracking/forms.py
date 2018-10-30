from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from django import forms
from .models import Tracking, Element


class EventForm(forms.ModelForm):

    class Meta:
        model = Tracking
        fields = ['date','start_time','end_time', 'categories', 'element', 'notiz']
        widgets = {
            'date': DatePickerInput(),
            'start_time': TimePickerInput(),
            'end_time': TimePickerInput(),
            'notiz': forms.TextInput(attrs={'size': '30'})
        }

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

