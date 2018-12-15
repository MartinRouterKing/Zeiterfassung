from tracking.models import Categorie, Workingtime, Categorie
from calender.models import CalendarEvent
from django.shortcuts import render
from datetime import datetime

def Analyticsview(request):

    '''
    Get the contractual working time per month from database
    '''
    try:
        working_time = Workingtime.objects.filter(user_id=request.user.id)
        working_time = int(working_time.values_list('workingtime')[0][0] * 4.35)
    except:
        working_time = 1

    '''
    Calculation the current month for further calculations
    '''
    currentmonth = datetime.now().month

    '''
    Get the working data from the database and calculation of the 
    workingtime per month.
    
        obj             -> working data objects
        obj_data        -> working date 
        obj_hours       -> working hours
        obj_categories  -> categories of the working activity
    '''
    obj = CalendarEvent.objects.filter(user_id=request.user.id)
    obj_date = obj.values_list('start')
    obj_hours = obj.values_list('hours')
    obj_categories = obj.values_list('type')
    list_hours = []

    for i in range(1, 13):
        a = 0
        for date, hour in zip(obj_date, obj_hours):
            if i == date[0].month:
                a = a + hour[0]
        list_hours.append(a)


    '''
    Calculation working time per month in percent
    '''
    from django.db.models import Sum

    hours_user = CalendarEvent.objects.filter(user_id=request.user.id)
    hours_user_month = hours_user.filter(start__month=currentmonth).aggregate(Sum('hours'))


    if hours_user_month['hours__sum'] is not None:
        working_time_perc = int(hours_user_month['hours__sum']/working_time * 100)
        print(working_time_perc)
    else:
        working_time_perc = 0



    '''
    Calculation overtime for the current month.
    '''

    #if working_time < list_hours[currentmonth-2]:
    #  overtime = (list_hours[currentmonth]-working_time)/100
    #else:
    #    overtime = 0


    '''
    calculation of the working hours per categorie for the last 
    3 month
    '''

    list_cat = []
    list_cat_label= []


    for c in list(set(Categorie.objects.all().values_list('cat',flat=True))):

        h = 0
        for hour, cat in zip(obj_hours, obj_categories):
            print(cat[0])
            print(c)
            print("__")
            if cat[0] == c:
                print('equal')
                print(hour[0])
                h = h + (hour[0] / sum(list_hours))*100
                h = round(h, 2)
        list_cat_label.append(c)
        list_cat.append(h)

    print(list_cat)
    print(list_cat_label)
    user = request.user

    return render(request, 'home.html',{
        'user': user,
        'list_hours': list_hours,
        'list_cat_label': list_cat_label,
        'list_cat': list_cat,
        'working_time_prec': working_time_perc,
    })


def load_canvas(request):

    if request.method == 'GET':
        type = request.GET['selectedOption']
    type = type + '-chart'
    print(type)
    return render(request, 'load_canvas.html',
                  {'type': type}
                  )