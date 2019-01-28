from django.shortcuts import render
from .models import CalendarEvent, CalendarNote
from tracking.models import Categorie, Element, FavoriteElement, Workingtime
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import Serializer

def all_events(request):
    today = datetime.now()
    user = request.user
    year = today.year
    month =  today.month

    categorie = Categorie.objects.all()
    try:
        workingtime = Workingtime.objects.get(user_id=user).get_wk_employ_month()
    except ObjectDoesNotExist:
        workingtime = 0

    events = CalendarEvent.objects.filter(user_id=user, start__month=month, start__year=year).only("id", "type", "title", "type", "start", "end", "note", "all_day")

    event_notes = CalendarNote.objects.filter(user_id=user, start__month=month, start__year=year)

    try:
        event_id = CalendarEvent.objects.latest('id').id + 1
    except:
        event_id = 1
    try:
        event_notes_id = CalendarNote.objects.latest('id').id + 1
    except:
        event_notes_id = 1

    context = {
        'year': year,
        'workingtime': workingtime,
        'user': user,
        'categorie': categorie,
        "event_notes": event_notes,
        "events": events,
        "latest_note_id": event_notes_id,
        "latest_id": event_id
    }

    return render(request,'calender/calender.html', context)

def postview(request):

    if request.method == 'POST':
        event_type = request.POST['save']
        action = request.POST['action']
        if action == 'save':
            user_id = User.objects.get(id=request.user.id)

            if event_type == "note":
                title = request.POST['title']
                title = title.replace('\n', "")
                start = request.POST['start']
                end = request.POST['end']
                id = request.POST['id'].split("_")[1]
                start = datetime.strptime(start, '%a %b %d %Y %H:%M:%S %Z%z')
                end = datetime.strptime(end, '%a %b %d %Y %H:%M:%S %Z%z')

                n = CalendarNote(
                    user_id=user_id,
                    title=title,
                    start=start,
                    end=end
                )
                n.id=id
                n.save()


            else:
                id = request.POST['id']
                title = request.POST['title']
                type = request.POST['type']
                start = request.POST['start']
                end = request.POST['end']
                note = request.POST['note']
                note = note.replace('\n', "")

                start = datetime.strptime(start, '%a %b %d %Y %H:%M:%S %Z%z')
                end = datetime.strptime(end, '%a %b %d %Y %H:%M:%S %Z%z')



                hours = (end - start).seconds/3600

                '''
                The Event-ypes are first initialized with their id as int.
                In the Database we need the string value and for the later changing of Events on
                the calendar we need to use the following exception to check wetther the type is a string
                or and int. 
                
                '''
                try:
                    type = int(type)
                    type = Categorie.objects.filter(id=type).values_list('cat', flat=True)
                except (ValueError):
                    type = [type]


                calc = Element.objects.filter(element__kat_element=title, categories__cat=type[0]).values_list('calc__calc', flat=True)


                q = CalendarEvent(
                    user_id=user_id,
                    title=str(title),
                    type=type[0],
                    start=start,
                    end=end,
                    calc=calc[0],
                    hours=hours,
                    note= note,
                    all_day=False)

                q.id = id
                q.save()

        if action == 'delete':
            if event_type == "event":
                id = request.POST['id']

                instance = CalendarEvent.objects.get(id=id)
                instance.delete()

            elif event_type == "note":

                id = request.POST['id'].split("_")[1]
                instance = CalendarNote.objects.get(id=id)
                instance.delete()

    return render(request,'calender/calender.html',{})

def load_elements(request):
    if request.method == 'GET':
        categories_id = request.GET['categories']
        checked = request.GET['checked']

        if checked == 'false':
            element = Element.objects.filter(categories_id=categories_id).order_by('categories')
        else:
            element = FavoriteElement.objects.filter(fav_element__categories_id=categories_id)

    return render(request, 'calender/element_events.html',
                  {
                      'element': element,
                      'checked': checked
                  })