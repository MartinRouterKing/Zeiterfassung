from django.shortcuts import render
from django.http import HttpResponse
from .models import CalendarEvent
from tracking.models import Categorie, Element
from fullcalendar.util import events_to_json, calendar_options
import datetime
import json
import dateutil.parser

# This is just an example for this demo. You may get this value
# from a separate file or anywhere you want

OPTIONS = """{
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'month,agendaWeek,agendaDay'
    },
    
    editable: true,
    droppable: true, // this allows things to be dropped onto the calendar
    drop: function() {
      // is the "remove after drop" checkbox checked?
      if ($('#drop-remove').is(':checked')) {
        // if so, remove the element from the "Draggable Events" list
        $(this).remove();
      }
    }"""

#def index(request):
#    event_url = 'all_events/'
#    return render(request, 'demo/index.html',{})

#def all_events(request):
#    events = CalendarEvent.objects.all()
#    return HttpResponse(events_to_json(events), content_type='application/json')

from .forms import CalenderForm

def all_events(request):

    categorie = Categorie.objects.all()
    events = CalendarEvent.objects.all()
    get_event_types = CalendarEvent.objects.only('title')

    context = {
        'categorie': categorie,

        "events": events,
        "get_event_types": get_event_types,
    }

    return render(request,'index.html', context)

def postview(request):

    if request.method == 'POST':
        action = request.POST['action']
        if action == 'save':
            print('save')
            title = request.POST['title']
            start = request.POST['start']
            end = request.POST['end']
            start = datetime.datetime.strptime(start, '%a %b %d %Y %H:%M:%S %Z%z')
            end = datetime.datetime.strptime(end, '%a %b %d %Y %H:%M:%S %Z%z')
            print(title)
            print(start)
            print(end)
            print("time_change")
            print(start.date())
            print(start.time())

        if action == 'delete':
            print('delete')

    return render(request,'index.html',{})

def load_elements(request):
    if request.method == 'GET':
        categories_id = request.GET['categories']
    element = Element.objects.filter(categories_id=categories_id).order_by('categories')
    print(element)
    return render(request, 'element_events.html',
                  {
                      'element': element
                  })