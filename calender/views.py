from django.shortcuts import render
from .models import CalendarEvent
from tracking.models import Categorie, Element, FavoriteElement
from datetime import datetime, timedelta
from django.contrib.auth.models import User

def all_events(request):
    today = datetime.now() - timedelta(days=14)
    categorie = Categorie.objects.all()
    events = CalendarEvent.objects.filter(user_id = request.user)
    print(events)
    events.filter(start__gte=today)
    get_event_types = CalendarEvent.objects.only('title')
    user = request.user
    try:
        event_id = CalendarEvent.objects.latest('id').id + 1
    except:
        event_id = 1

    print(events)

    context = {
        'user': user,
        'categorie': categorie,
        "events": events,
        "latest_id": event_id,
        "get_event_types": get_event_types,
    }

    return render(request,'index.html', context)

def postview(request):

    if request.method == 'POST':
        action = request.POST['action']
        if action == 'save':
            id = request.POST['id']
            title = request.POST['title']
            type = request.POST['type']
            start = request.POST['start']
            end = request.POST['end']
            note = request.POST['note']
            start = datetime.strptime(start, '%a %b %d %Y %H:%M:%S %Z%z')
            end = datetime.strptime(end, '%a %b %d %Y %H:%M:%S %Z%z')

            print(id)
            print(title)
            print(type)


            hours = (end - start).seconds/3600
            print(hours)
            user_id = User.objects.get(id=request.user.id)
            cat = Categorie.objects.get(id=type)

            type = Categorie.objects.filter(id=type).values_list('cat', flat=True)
            print(type)
            print(title)

            q = CalendarEvent(
                user_id=user_id,
                title=str(title),
                type=type[0],
                start=start,
                end=end,
                hours=hours,
                note=note,
                all_day=False)

            q.id = id
            q.save()

        if action == 'delete':

            id = request.POST['id']
            print(id)

            instance = CalendarEvent.objects.get(id=id)
            print(instance.id)
            instance.delete()

    return render(request,'index.html',{})

def load_elements(request):
    if request.method == 'GET':
        categories_id = request.GET['categories']
        checked = request.GET['checked']
        print(checked)

        if checked == 'false':
            element = Element.objects.filter(categories_id=categories_id).order_by('categories')
        else:
            element = FavoriteElement.objects.filter(fav_element__categories_id=categories_id)

    return render(request, 'element_events.html',
                  {
                      'element': element,
                      'checked': checked
                  })