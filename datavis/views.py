from tracking.models import Categorie, Workingtime, Categorie
from calender.models import CalendarEvent
from django.shortcuts import render
from datetime import datetime
from django.db.models import Sum

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
    month_name_list = ["Unbekannt" ,"Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
    currentmonth_name = month_name_list[currentmonth]
    currentyear = datetime.now().year

    '''
    Get the working data from the database and calculation of the 
    workingtime per month.
    
        obj             -> working data objects
        obj_data        -> working date 
        obj_hours       -> working hours
        obj_categories  -> categories of the working activity
    '''
    obj = CalendarEvent.objects.filter(user_id=request.user.id, start__year=currentyear)
    obj_date = obj.values_list('start')
    obj_hours = obj.values_list('hours', flat=True)
    obj_categories = obj.values_list('type')
    list_hours = []

    for i in range(1, 13):
        a = 0
        for date, hour in zip(obj_date, obj_hours):
            if i == date[0].month:
                a = a + float(hour)
        list_hours.append(a)

    '''
    Calculation working time per month in percent
    '''


    hours_user = CalendarEvent.objects.filter(user_id=request.user.id)
    hours_user_month = hours_user.filter(start__month=currentmonth).aggregate(Sum('hours'))


    if hours_user_month['hours__sum'] is not None:
        working_time_perc = int(hours_user_month['hours__sum']/working_time * 100)
        print(working_time_perc)
    else:
        working_time_perc = 0


    '''
    calculation of the working hours per categorie for the last 
    3 month
    '''

    list_cat = []
    list_cat_label= []
    colors = ['#1abc9c', '#34495e', '#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6', "#bccad6", "#8d9db6", "#667292", "#f1e3dd", "#cfe0e8","#b7d7e8","#87bdd8","#daebe8"]


    for c in list(set(Categorie.objects.all().values_list('cat',flat=True))):
        h = 0
        for hour, cat in zip(obj_hours, obj_categories):
            if cat[0] == c:
                h = h + (float(hour) / sum(list_hours))*100
                h = round(h, 2)
        list_cat_label.append(c)
        list_cat.append(h)

    user = request.user
    data = {}
    counter = 0
    for c in list(set(Categorie.objects.all().values_list('cat', flat=True))):
        data_list = []
        event = CalendarEvent.objects.filter(start__year=currentyear,
                                             user_id__username=user,
                                             start__month=currentmonth,
                                             type=c).aggregate(Sum('hours'))['hours__sum']
        if event==None:
            data_list.append(0)
        else:
            data_list.append(float(event))

        if len(c)>30:
            data[c[:30] + "..."] = []
            data[c[:30] + "..."].append(data_list)
            data[c[:30] + "..."].append(colors[counter])
        else:
            data[c] = []
            data[c].append(data_list)
            data[c].append(colors[counter])

        counter += 1

    currentdate = str(currentmonth) + "." + str(currentyear)
    return render(request, 'datavis/home.html',{
        'currentdate': currentdate,
        'currentmonth_name': currentmonth_name,
        'data': data,
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
    return render(request, 'datavis/load_canvas.html',
                  {'type': type}
                  )

def load_bar_cat(request):
    if request.method=='GET':
        date = request.GET['selectedDate']
        date_iso = datetime.strptime(date + " +0000", '%m.%Y %z')
        date_iso.isoformat()


        user = request.user

        colors = ['#1abc9c', '#34495e', '#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#95a5a6',
                  "#bccad6", "#8d9db6", "#667292", "#f1e3dd", "#cfe0e8", "#b7d7e8", "#87bdd8", "#daebe8"]

        data = {}
        counter = 0
        for c in list(set(Categorie.objects.all().values_list('cat', flat=True))):
            data_list = []
            event = CalendarEvent.objects.filter(start__year=date_iso.year,
                                                 user_id__username=user,
                                                 start__month=date_iso.month,
                                                 type=c).aggregate(Sum('hours'))['hours__sum']

            if event == None:
                data_list.append(0)
            else:
                data_list.append(float(event))

            if len(c) > 30:
                data[c[:30] + "..."] = []
                data[c[:30] + "..."].append(data_list)
                data[c[:30] + "..."].append(colors[counter])
            else:
                data[c] = []
                data[c].append(data_list)
                data[c].append(colors[counter])

            counter += 1


    return render(request, 'datavis/load_bar_cat.html',
                  {'data': data}
                  )