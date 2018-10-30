from bootstrap_datepicker_plus import TimePickerInput
from django import forms

from .models import CalendarEvent

class CalenderForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ['title', 'start', 'end']
