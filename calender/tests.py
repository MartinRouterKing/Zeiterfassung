from django.test import TestCase
import datetime
from datetime import timedelta
import pytz
from .models import CalendarEvent
from django.contrib.auth.models import User
from tracking.models import Element
from random import randint

# Generate Test Data

def generateEventData(days, user):
    user_obj = User.objects.get(id=user)
    today = pytz.utc.localize(datetime.datetime.utcnow())
    today = today.replace(hour=6, minute=0, second=0)
    today = today.replace(day=1)
    ids = Element.objects.all().values_list("id", flat=True)
    count = 0
    for day in range(days):
        today = today.replace(hour=8, minute=0, second=0)
        print(day)
        element_obj = Element.objects.get(id=ids[randint(0, len(ids)-1)])
        for h in range(4):
            count =+ 1
            if today.weekday() == 5 or today.weekday()==6:
                continue
            else:
                    q = CalendarEvent(
                        user_id=user_obj,
                        event_id = count ,
                        type=element_obj.categories,
                        title=element_obj.element,
                        calc=element_obj.calc,
                        note="Das ist eine Test Notiz!",
                        all_day=False,
                        start= today,
                        end= today + timedelta(hours=2),
                        hours=2
                    )
                    print(q)
                    q.save()

            today = today + timedelta(hours=2)

        today = today + timedelta(days=1)
