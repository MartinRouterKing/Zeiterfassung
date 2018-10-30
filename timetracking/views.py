from tracking.models import Tracking, Element
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from tracking.forms import EventForm
import datetime
from django.contrib import messages
from django.core.exceptions import ValidationError

def input(request):

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            try:
                date = form.cleaned_data['date']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                categories = form.cleaned_data['categories']
                element = form.cleaned_data['element']
                notiz = form.cleaned_data['notiz']

                try:
                    # Create datetime objects for each time (a and b)
                    dateTimeA = datetime.datetime.combine(datetime.date.today(), end_time)
                    dateTimeB = datetime.datetime.combine(datetime.date.today(), start_time)
                    # Get the difference between datetimes (as timedelta)
                    dateTimeDiff = dateTimeA - dateTimeB

                    a = ':'.join(str(dateTimeDiff).split(":")[:2])
                    user = User.objects.get(id=request.user.id)

                    t = Tracking(user_id=user,
                                 date=date,
                                 start_time=start_time,
                                 end_time=end_time,
                                 hours=a,
                                 categories=categories,
                                 element=element,
                                 notiz=notiz)
                    t.save()

                    messages.success(request, ' Erfolgreich gespeichert')


                except (ValueError, TypeError, ValidationError):
                    messages.warning(request, 'Bitte Prüfen Sie die Zeitangaben')

            except (ValueError, TypeError, ValidationError):
                messages.warning(request, 'Bitte alle Felder ausfüllen')

            return render(request, 'input.html', {
                'form': form
            })



    else:
        form = EventForm()


    return render(request, 'input.html', {
        'form': form
    })

def load_elements(request):
    categories_id = request.GET.get('categories')
    print(categories_id)
    element = Element.objects.filter(categories_id=categories_id).order_by('categories')
    print(element)
    return render(request, 'input_element_list_options.html',
                  {'element': element}
                  )















